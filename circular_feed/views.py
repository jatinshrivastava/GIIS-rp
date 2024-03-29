from django.shortcuts import render
from circular_feed.models import Circular

def circular_index(request):
    circular = Circular.objects.all().order_by('-created_on')
    context = {
        "circulars": circular,
    }
    return render(request, "circular_index.html", context)

def circular_detail(request, pcircular):
    circular = Circular.objects.get(pk=pcircular)
    context = {
        "circular": circular,
    }

    return render(request, "circular_detail.html", context)