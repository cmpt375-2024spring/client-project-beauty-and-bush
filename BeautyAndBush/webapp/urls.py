from . import views

from django.urls import path


urlpatterns = [
    path('moodboard/', views.MoodBoardView, name='moodboard'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('memberships/', views.memberships, name='memberships'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('login/', views.login, name='login'),
    path('my-account/', views.my_account, name='my-account'),
    path('history/', views.history, name='history'),
    path('faq/', views.faq, name='faq'),
    path('book-now-slc/', views.book_now_slc, name='slc'),
    path('book-now-st-george/', views.book_now_st_george, name='st_george')
]
