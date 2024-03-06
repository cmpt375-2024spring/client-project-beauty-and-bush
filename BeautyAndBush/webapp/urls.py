from . import views

from django.urls import path


urlpatterns = [
    path('moodboard/', views.MoodBoardView, name='moodboard'),
]