# Generated by Django 2.2.12 on 2020-11-19 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_auto_20201119_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='set',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='flashcards.Set'),
        ),
        migrations.AddField(
            model_name='set',
            name='language',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='flashcards.Language'),
        ),
    ]
