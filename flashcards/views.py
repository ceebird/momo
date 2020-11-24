from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card, Set
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView
from django.core import serializers

import json
import pprint
import requests
import random

class IndexView(generic.ListView):
    template_name = 'flashcards/index.html'
    model = Set
    context_object_name = 'sets'

class CardCreate(CreateView):
    model = Card
    fields = ['set', 'language_word', 'native_word']

class CardUpdate(UpdateView):
    model = Card
    fields = ['language_word', 'native_word']
    template_name_suffix = '_update_form'

class SetCreate(CreateView):
    model = Set
    fields = ['name', 'language']

# --------- View rendering functions --------- #
def set_view(request, pk):
    """
        Renders Set View
    """
    return render(request, 'flashcards/set.html', {
        'cards': Card.objects.filter(set=pk),
        'set_id': pk,
    })

def cards_start(request, set_id):
    """
        Renders flashcards view 
    """
    return render(request, 'flashcards/cards.html', {
        'set_id': set_id,
    })

def word_search(request, set_id):
    """
        Calls word search view
    """
    return render(request, 'flashcards/word_search.html', {
        'set_id': set_id,
    })

#--------- Flashcard js functions ---------#

def answer(request, set_id):
    """
        Checks submitted card answer to see if correct
    """
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
    """
        Collects next card from passed id
    """
    try:
        if request.method == 'POST':
            next_card = Card.objects.get(pk=int(request.POST['card_id']))
            return HttpResponse(
                json.dumps({"pk": next_card.pk, "front_word" : next_card.language_word, "back_word": next_card.native_word }),
                content_type="application/json"
            )
    except:
        return HttpResponse(
                json.dumps({"next_card": False}),
                content_type="application/json"
            )

def get_cards(request, set_id):
    """
        Returns a randomised array of ids for cards of set and the values of first card
    """
    cards = Card.objects.filter(set=set_id)
    ids = [ card.id for card in cards ]

    # Randomise cards
    random.shuffle(ids)
    card = Card.objects.get(pk=ids[0])
    return HttpResponse(
            json.dumps({"card_ids": ids, 'first_card': {'pk': card.pk, 'front_word': card.language_word, 'back_word' : card.native_word}}),
            content_type="application/json"
        )
        
def search_word(request, set_id):
    """
        Gets word from form and passes to the Merriam Webster API. returning result of search
    """
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
