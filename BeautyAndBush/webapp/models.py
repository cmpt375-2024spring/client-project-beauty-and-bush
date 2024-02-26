from django.db import models
from django.shortcuts import render


def MoodBoardView(request):
    return render(request, 'webapp/moodboard.html')