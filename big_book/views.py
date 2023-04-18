from django.shortcuts import render
from django.conf import settings

from .models import *


def home(request):
    news = News.objects.all()
    reviews = Reviews.objects.all()
    studies = Studies.objects.all()
    context = {'news': news, 'reviews': reviews, 'studies': studies}
    return render(request, 'home.html', )


def about(request):
    return render(request, 'about.html')


def what_we(request):
    return render(request, 'what_we.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
