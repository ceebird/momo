# Generated by Django 3.1 on 2020-11-21 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_auto_20201119_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='set',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='flashcards.set'),
        ),
    ]
