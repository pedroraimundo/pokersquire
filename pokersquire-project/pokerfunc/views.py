from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def squire(request):

    data = request.POST.items()

    context = dict([(key, value) for key, value in data])
    print(context.keys(), ":", context.values())

    return render(request, 'squire.html', {'context': context})


def settings(request):
    return render(request, 'settings.html')


def results(request):
    return render(request, 'results.html')
