from django.urls import path
from . import views

urlpatterns = [
    path('moodboard/', views.MoodBoardView, name='moodboard'),
    # Add other URL patterns as needed
]