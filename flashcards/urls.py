from django.urls import path

from . import views

app_name = 'flashcards'
urlpatterns = [
    # Set
    path('', views.IndexView.as_view(), name='index'),
    path('create_set/', views.SetCreate.as_view(), name='create_set'),
    path('set/<int:pk>/', views.set_view, name='set_view'),

    # Card
    path('set/<int:set_id>/cards/', views.cards_start, name='cards_start'),
    path('set/<int:set_id>/update_card/<int:pk>', views.CardUpdate.as_view(), name='update_card'),
    path('set/<int:set_id>/create_card', views.CardCreate.as_view(), name='create_card'),
    path('set/<int:set_id>/cards/get_cards/', views.get_cards, name='get_cards'),
    path('set/<int:set_id>/cards/answer/', views.answer, name='answer'),
    path('set/<int:set_id>/cards/next_card/', views.next_card, name='next_card'),

    # Word Search
    path('set/<int:set_id>/search_word/', views.search_word, name='search_word'),
    path('set/<int:set_id>/word_search/', views.word_search, name='word_search'),
    path('set/<int:set_id>/word_search/search_word/', views.search_word, name='search_word'),
]
