# Generated by Django 2.2.12 on 2020-11-19 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_auto_20201119_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='set',
        ),
        migrations.RemoveField(
            model_name='set',
            name='language',
        ),
    ]
