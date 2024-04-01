from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import generic


def index(request):
    return render(request, 'webapp/index.html')


def about(request):
    return render(request, 'webapp/about.html')


def services(request):
    return render(request, 'webapp/services.html')


def memberships(request):
    return render(request, 'webapp/memberships.html')


def contact_us(request):
    return render(request, 'webapp/contact_us.html')


def my_account(request):
    return render(request, 'webapp/my_account.html')


def history(request):
    return render(request, 'webapp/history.html')


def faq(request):
    return render(request, 'webapp/faq.html')


def st_george_home(request):
    return render(request, 'webapp/st_george_home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'webapp/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my-account')
    else:
        form = AuthenticationForm()
    return render(request, 'webapp/login.html', {'form': form})
