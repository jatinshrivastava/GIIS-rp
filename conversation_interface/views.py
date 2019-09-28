from django.shortcuts import render

def conversation_index(request):
    return render(request, 'conversation_index.html', {})