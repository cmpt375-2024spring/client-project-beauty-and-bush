from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import MyAccount

from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.http import JsonResponse

User = get_user_model()
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
    account = MyAccount.objects.get(user=request.user)
    if request.method == 'POST':
        # Update the account fields with the new values from the form
        account.name = request.POST.get('name')
        account.email = request.POST.get('email')
        account.purchase_history = request.POST.get('purchase_history')
        account.wallet = request.POST.get('wallet')
        account.save()  # Save the changes to the database
        return redirect('my-account')
    return render(request, 'webapp/my_account.html', {'account': account})


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
            user = form.save()
            MyAccount.objects.create(user=user)
            login(request, user)
            return redirect('my-account')
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
                account = MyAccount.objects.get(user=user)
                return render(request, 'webapp/my_account.html', {'account': account})
    else:
        form = AuthenticationForm()
    return render(request, 'webapp/login.html', {'form': form})


def forgot_password(request):
    return render(request, 'webapp/forgot_password.html')


def reset_password(request):
    return render(request, 'webapp/reset_passord.html')


def password_reset_confirmation(request):
    return render(request, 'webapp/reset_confirmation.html')


def check_email_existence(request):
    email = request.GET.get('email', None)
    if email:
        # Check if email exists in the database
        email_exists = User.objects.filter(email=email).exists()
        return JsonResponse({'exists': email_exists})
    else:
        # Invalid request, email parameter not provided
        return JsonResponse({'error': 'Email parameter not provided'}, status=400)