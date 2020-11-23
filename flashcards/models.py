from django.db import models
from django.urls import reverse

class Language(models.Model):

    name = models.CharField(max_length=200, default="Spanish")

    def __str__(self):
        return self.name

class Set(models.Model):

    language = models.ForeignKey(Language, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flashcards:set_view', args=[self.id])

class Card(models.Model):
    language_word = models.CharField(max_length=200)
    native_word = models.CharField(max_length=200)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, default="", related_name='cards')

    def __str__(self):
        return f"{self.set.name}: {self.language_word}"

    def get_absolute_url(self):
        return reverse('flashcards:card_view', args=[self.id])