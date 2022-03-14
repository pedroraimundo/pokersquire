from django.shortcuts import render, get_object_or_404
from .models import Stats


def squire(request):
    stats = Stats.objects
    return render(request, 'squire.html', {'stats': stats})