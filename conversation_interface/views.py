from django.shortcuts import render, redirect
from circular_feed.models import Circular
from conversation_interface.models import Message, MessageStatus
from users.models import CustomUser
from conversation_interface.forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from itertools import product
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required(login_url='/users/login/')
def conversation_index(request, pcircular):
    user_type = request.user.user_type
    if (user_type=='St'):
        messageOfParticularCircular = MessageStatus.objects.filter(circular_id=pcircular).order_by('-created_on')
        circular = Circular.objects.get(pk=pcircular)
        users = CustomUser.objects.all()
        context = {
            "messageOfParticularCircular": messageOfParticularCircular,
            "circular": circular,
            "users" : users,
        }
        return render(request, "conversation_index.html", context)
    else:
        return redirect('unauthorized')

@login_required(login_url='/users/login/')
def messages(request, pcircular, receiver):
    user_type = request.user.user_type
    if (user_type=='Pa'):
        staff_status = request.user.user_type
        circular = Circular.objects.get(pk=pcircular)
        field_exists = MessageStatus.objects.filter(Q(circular_id=pcircular) & Q(created_by= request.user.username)).exists()
        form = MessageForm()
        if 'satisfied' in request.POST:
            form = MessageForm(request.POST)
            if form.is_valid():
                if (field_exists == True):
                    id = MessageStatus.objects.filter(Q(circular_id=pcircular) & Q(created_by= request.user.username)).values('id')[0]['id']
                    MessageStatus.objects.filter(pk=id).update(status=MessageStatus.Closed)
                    MessageStatus.objects.filter(pk=id).update(last_message=form.cleaned_data["message"])
                    MessageStatus.objects.filter(pk=id).update(last_message_time=datetime.now())
                                
                else:
                    messageStats = MessageStatus(
                        created_by = request.user.username,
                        status = MessageStatus.Open,
                        circular_id=circular,
                        last_message = form.cleaned_data["message"],
                        last_message_time = datetime.now(),
                    )
                    messageStats.save()
                    
                compose = Message(
                    created_by = request.user.username,
                    created_for = receiver,
                    created_by_staff_username = 'none',
                    message=form.cleaned_data["message"],
                    circular_id=circular
                )
                compose.save()

            url = reverse('messages', kwargs={'pcircular':circular.pk , 'receiver':'staff'})
            return HttpResponseRedirect(url)
        elif 'send' in request.POST:
            form = MessageForm(request.POST)
            if form.is_valid():
                if (field_exists == True):
                    id = MessageStatus.objects.filter(Q(circular_id=pcircular) & Q(created_by= request.user.username)).values('id')[0]['id']
                    MessageStatus.objects.filter(pk=id).update(status=MessageStatus.Open)
                    MessageStatus.objects.filter(pk=id).update(last_message=form.cleaned_data["message"])
                    MessageStatus.objects.filter(pk=id).update(last_message_time=datetime.now())
                                
                else:
                    messageStats = MessageStatus(
                        created_by = request.user.username,
                        status = MessageStatus.Open,
                        circular_id=circular,
                        last_message = form.cleaned_data["message"],
                        last_message_time = datetime.now(),
                    )
                    messageStats.save()

                compose = Message(
                    created_by = request.user.username,
                    created_for = receiver,
                    created_by_staff_username = 'none',
                    message=form.cleaned_data["message"],
                    circular_id=circular
                )
                compose.save()
            url = reverse('messages', kwargs={'pcircular':circular.pk , 'receiver':'staff'})
            return HttpResponseRedirect(url)
        
        username = request.user.username
        messages_from = receiver
        from_current = Message.objects.filter(created_by=username)
        same_sender = Message.objects.filter(created_for=username)
        created_by_specific_parent = Message.objects.filter(created_by=messages_from)
        same_circular = Message.objects.filter(circular_id=circular)
        own_messages = same_sender | from_current
        for_staff = own_messages & created_by_specific_parent
        compose = own_messages & same_circular
        composes = compose.all().order_by('created_on')  
        users = CustomUser.objects.get(username=username)
        context = {
            "circular": circular,
            "composes": composes,
            "form": form,
            "users" : users
        }
        
        return render(request, 'messages.html', context)
    else:
        return redirect('unauthorized')
    
@login_required(login_url='/users/login/')
def staff_messages(request, pcircular, receiver):
    user_type = request.user.user_type
    if (user_type=='St'):
        circular = Circular.objects.get(pk=pcircular)
        message_status_field = MessageStatus.objects.filter(Q(circular_id=pcircular) & Q(created_by= receiver))
        field_exists = message_status_field.exists()
        form = MessageForm()
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                if (field_exists == True):
                    id = MessageStatus.objects.filter(Q(circular_id=pcircular) & Q(created_by= receiver)).values('id')[0]['id']
                    MessageStatus.objects.filter(pk=id).update(status=MessageStatus.Waiting_for_acknowledgement)
                    MessageStatus.objects.filter(pk=id).update(last_message=form.cleaned_data["message"])
                    MessageStatus.objects.filter(pk=id).update(last_message_time=datetime.now())
                                
                else:
                    pass
            
                compose = Message(
                    created_by = 'Staff',
                    created_for = receiver,
                    created_by_staff_username = request.user.username,
                    message=form.cleaned_data["message"],
                    circular_id=circular
                )
                compose.save()
                
            url = reverse('staff_messages', kwargs={'pcircular':circular.pk , 'receiver':receiver})
            return HttpResponseRedirect(url)
        
        staff_status = request.user.user_type
        username = 'Staff'
        messages_from = receiver
        from_specific_parent = Message.objects.filter(created_by=messages_from)
        created_for_specific_parent = Message.objects.filter(created_for=messages_from)
        created_by_staff = Message.objects.filter(created_by=username)
        same_circular = Message.objects.filter(circular_id=circular)
        intersection1 = from_specific_parent & same_circular
        intersection2 = created_by_staff & created_for_specific_parent & same_circular
        compose = intersection1 | intersection2
        users = CustomUser.objects.get(username=messages_from)
        composes =compose.all().order_by('created_on')
        id = MessageStatus.objects.filter(Q(circular_id=pcircular) & Q(created_by= receiver)).values('id')[0]['id']
        message_status_data = MessageStatus.objects.get(pk=id)
        if ( message_status_data.status == 'Closed'):
            context = {
                "circular": circular,
                "composes": composes,
                "users" : users,
                "message_status_data" : message_status_data,
            }
        else:
            context = {
                "circular": circular,
                "composes": composes,
                "form": form,
                "users" : users,
                "message_status_data" : message_status_data,
            }
        
        return render(request, 'messages.html', context)
    else:
        return redirect('unauthorized')

def unauthorized(request):
  
  return render(request, 'unauthorized.html')
