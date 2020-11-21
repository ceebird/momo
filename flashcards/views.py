from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card, Set
from django.template import loader
from django.urls import reverse
from django.views import generic
import json


class IndexView(generic.ListView):
    template_name = 'flashcards/index.html'
    context_object_name = 'cards'

    def get_queryset(self):
        """Return all cards."""
        return Card.objects.all()

class SetView(generic.DetailView):
    model = Set
    template_name = 'flashcards/set.html'

    def get_cards(self):
        """Return all cards of set."""
        return self.cards.all


class CardView(generic.DetailView):
    model = Card
    template_name = 'flashcards/card.html'

def answer(request, card_id):
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
        # try:
            # answer = request.POST.get['answer']
            # print(answer)
        #     if card.native_word.lower() == answer.lower():
        #         try:
        #             next_card = Card.objects.get(pk=card_id+1)
        #             return HttpResponseRedirect(reverse('flashcards:card_view', args=(next_card.id,)))
        #         except:
        #             return HttpResponseRedirect(reverse('flashcards:card_view', args=(1,)))
        #     else:
        #         return render(request, 'flashcards/card.html', {
        #             'card': card,
        #             'wrong_answer': "Incorrect!",
        #         })
                
        # except:
        #     return render(request, 'flashcards/card.html', {
        #         'card': card,
        #         'error_message': "Couldn't submit",
        #     })
        else:
            return HttpResponse(
                json.dumps({"correct_answer": False}),
                content_type="application/json"
            )

def next_card(request, card_id):
    try:
        next_card = Card.objects.get(pk=card_id+1)
        # return HttpResponseRedirect(reverse('flashcards:card_view', args=(next_card.id,)))
        # return HttpResponse(
        #         json.dumps({'next_card_pk': next_card.pk}),
        #         content_type="application/json"
        #     )
        return HttpResponse(
            json.dumps({"pk": next_card.pk, "front_word" : next_card.language_word, "back_word": next_card.native_word }),
            content_type="application/json"
        )
    except:
        return HttpResponseRedirect(reverse('flashcards:card_view', args=(1,)))
            

def first_card(request, card_id):
    card = get_object_or_404(Card, pk=1)
    return HttpResponse(
            json.dumps({"pk": card.pk, "front_word" : card.language_word, "back_word": card.native_word }),
            content_type="application/json"
        )