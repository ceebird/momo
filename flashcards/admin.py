from django.contrib import admin

from .models import Language, Set, Card

admin.site.register(Language)
admin.site.register(Set)
# admin.site.register(Card)

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['set']}),
        ('Words', {'fields': ['language_word', 'native_word']}),
    ]
    list_display = ('language_word', 'native_word', 'set')

admin.site.register(Card, CardAdmin)