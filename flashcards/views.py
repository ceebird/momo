from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card, Set
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.views.generic.edit import CreateView
import requests

import json
import pprint

class IndexView(generic.ListView):
    template_name = 'flashcards/index.html'
    model = Set
    context_object_name = 'sets'

class CardCreate(CreateView):
    model = Card
    fields = ['set', 'language_word', 'native_word']

def set_view(request, pk):
    return render(request, 'flashcards/set.html', {
        'cards': Card.objects.all(),
        'set_id': pk,
    })

def card_view(request, set_id):
    return render(request, 'flashcards/card.html', {
        'set_id': 1,
    })

def word_search(request, set_id):
    return render(request, 'flashcards/word_search.html', {
        'set_id': 1,
    })

def answer(request, set_id):
    if request.method == 'POST':
        card = get_object_or_404(Card, pk=int(request.POST['card_id']))
        response_data = {}
        answer = request.POST['answer_text']
        if card.native_word.lower() == answer.lower():
            response_data['correct_answer'] = True
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"correct_answer": False}),
                content_type="application/json"
            )

def next_card(request, set_id):
    try:
        if request.method == 'POST':
            next_card = Card.objects.get(pk=int(request.POST['card_id'])+1)
            return HttpResponse(
                json.dumps({"pk": next_card.pk, "front_word" : next_card.language_word, "back_word": next_card.native_word }),
                content_type="application/json"
            )
    except:
        return HttpResponse(
                json.dumps({"next_card": False}),
                content_type="application/json"
            )


def first_card(request, set_id):
    card = get_object_or_404(Card, pk=1)
    return HttpResponse(
            json.dumps({"pk": card.pk, "front_word" : card.language_word, "back_word": card.native_word }),
            content_type="application/json"
        )
        
def search_word(request, set_id):
    if request.method == 'POST':
        result = {}
        word = request.POST['word']

        if word:
            endpoint = 'https://dictionaryapi.com/api/v3/references/spanish/json/{word_id}?key={key}'
            url = endpoint.format(key=settings.MERRIAM_WEBSTER_APP_ID, word_id=word)
            response = requests.get(url)
            result = response.json()

            if response.status_code == 200:
                result = response.json()
                result.append({'message': False})
            else:
                if response.status_code == 404:
                    result.append({'message': 'No entry found for "%s"' % word})
                else:
                    result.append({'message': 'The Merriam Webster API is not available at the moment. Please try again later.'})
            return HttpResponse(
                json.dumps(result),
                content_type="application/json"
            )