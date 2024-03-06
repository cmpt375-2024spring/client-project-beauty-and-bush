from django.shortcuts import render


def MoodBoardView(request):
    return render(request, 'webapp/moodboard.html')


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


def login(request):
    return render(request, 'webapp/login.html')


def login(request):
    return render(request, 'webapp/login.html')


def my_account(request):
    return render(request, 'webapp/my_account.html')


def history(request):
    return render(request, 'webapp/history.html')


def faq(request):
    return render(request, 'webapp/faq.html')


def book_now_slc(request):
    return render(request, 'webapp/faq.html')


def book_now_st_george(request):
    return render(request, 'webapp/faq.html')
