from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'home.html', {'jobs': jobs})


def features(request):
    return render(request, 'features.html')


def about(request):
    return render(request, 'about.html')


def squire(request):
    return render(request, 'squire.html')