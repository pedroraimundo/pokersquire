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


def results(request):
    return render(request, 'results.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(exception):
    return render('500.html')
