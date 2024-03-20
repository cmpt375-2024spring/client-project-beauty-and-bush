from django.db import models
from django.db.models import Model
from django.shortcuts import render


def MoodBoardView(request):
    return render(request, 'webapp/moodboard.html')


def MyAccountView(Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    purchase_history = models.TextField(max_length=500)
    wallet = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.wallet} - {self.purchase_history}"
