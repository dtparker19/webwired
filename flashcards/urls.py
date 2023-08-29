from django.urls import path
from . import views

urlpatterns = [
    path('flashcards/', views.flashcards_list, name='flashcards_list'),
    path('flashcards/<int:flashcard_id>/', views.flashcard_detail, name='flashcard_detail'),
    path('flashcards/create/', views.create_flashcard, name='create_flashcard'),
]

