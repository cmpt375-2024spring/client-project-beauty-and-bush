from django.db import models
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()


def MoodBoardView(request):
    return render(request, 'webapp/moodboard.html')


class MyAccount(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    purchase_history = models.TextField(max_length=500)
    wallet = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.wallet} - {self.purchase_history}"
