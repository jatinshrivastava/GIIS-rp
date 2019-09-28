from django.shortcuts import render
from circular_feed.models import Circular
from conversation_interface.models import Compose
from conversation_interface.forms import ComposeForm
from django.contrib.auth.decorators import login_required
from itertools import product

@login_required(login_url='/account/login/')
def compose(request, pk):
    circular = Circular.objects.get(pk=pk)
    form = ComposeForm()
    if request.method == 'POST':
        form = ComposeForm(request.POST)
        if form.is_valid():
            compose = Compose(
                author=form.cleaned_data["author"],
                receiver=form.cleaned_data["receiver"],
                body=form.cleaned_data["body"],
                circular_id=circular
            )
            compose.save()
    username = request.user.username
    to_receiver = Compose.objects.filter(receiver=username)
    same_sender = Compose.objects.filter(author=username)
    same_circular = Compose.objects.filter(circular_id=circular)
    creator = same_sender | to_receiver
    composes = creator & same_circular
    composes.order_by('-created_on')
    context = {
        "circular": circular,
        "composes": composes,
        "form": form
    }
    
    return render(request, 'compose.html', context)







