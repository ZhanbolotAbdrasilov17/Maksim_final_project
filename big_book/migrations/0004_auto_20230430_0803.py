# Generated by Django 3.2 on 2023-04-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('big_book', '0003_auto_20230427_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='studies',
            name='desc_en',
            field=models.TextField(max_length=255, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='studies',
            name='desc_ru',
            field=models.TextField(max_length=255, null=True, verbose_name='Текст'),
        ),
    ]
