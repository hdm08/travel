from django.shortcuts import render
from .models import trv


# Create your views here.

def index(request):
    dest=trv.objects.all()

    return render(request, 'index.html',{'dests':dest})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def destinations(request):
    return render(request, 'destination.html')


def news(request):
    return render(request, 'news.html')
