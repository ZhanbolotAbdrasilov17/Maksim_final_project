from django.shortcuts import render
from django.conf import settings
from .forms import MailForm
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View


def home(request):
    news = News.objects.all()
    reviews = Reviews.objects.all()
    studies = Studies.objects.all()
    context = {'news': news, 'reviews': reviews, 'studies': studies}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def what_we(request):
    return render(request, 'what_we.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


class MailCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST)

        if form.is_valid():
            form.save()
            last_sender = Mail.objects.first()
            message = f'Имя: {last_sender.name}\n' \
                      f'Номер: {last_sender.phone}\n' \
                      f'Почта: {last_sender.email}\n' \
                      f'Текст: {last_sender.text}'

            send_mail(
                'Почта клиента или партнера',
                message,
                'oriyental.treyd@mail.ru',
                ['itpythonzhanbolot@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('home'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')