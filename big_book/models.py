from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Главная мысль')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class Reviews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=255, verbose_name="Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'


class Studies(models.Model):
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=255, verbose_name="Текст")

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = 'Исследования'
        verbose_name = 'Исследование'


class Mail(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Обращения клиентов'
        verbose_name = 'Обращение клиентов'