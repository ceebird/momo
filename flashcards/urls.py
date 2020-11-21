from django.urls import path

from . import views

app_name = 'flashcards'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('set/<int:pk>/', views.SetView.as_view(), name='set_view'),
    path('card/<int:pk>/', views.CardView.as_view(), name='card_view'),
    path('card/<int:card_id>/answer/', views.answer, name='answer'),
    path('card/<int:card_id>/next_card/', views.next_card, name='next_card'),
    path('card/<int:card_id>/first_card/', views.first_card, name='first_card'),
]

