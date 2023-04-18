# Generated by Django 4.2 on 2023-04-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Главная мысль')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.TextField(max_length=255, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.TextField(max_length=255, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Исследование',
                'verbose_name_plural': 'Исследования',
            },
        ),
    ]