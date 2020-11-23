from django.urls import path

from . import views

app_name = 'flashcards'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('set/<int:pk>/', views.set_view, name='set_view'),
    path('set/<int:set_id>/card/', views.card_view, name='card_view'),
    path('set/<int:set_id>/create', views.CardCreate.as_view(), name='create_card'),
    path('set/<int:set_id>/card/answer/', views.answer, name='answer'),
    path('set/<int:set_id>/card/next_card/', views.next_card, name='next_card'),
    path('set/<int:set_id>/card/first_card/', views.first_card, name='first_card'),
    path('set/<int:set_id>/card/search_word/', views.search_word, name='search_word'),
    path('set/<int:set_id>/card/word_search/', views.word_search, name='word_search'),
    path('set/<int:set_id>/card/word_search/search_word/', views.search_word, name='search_word'),
]
