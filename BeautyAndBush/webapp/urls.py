from . import views

from django.urls import path

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('services/', views.services, name='services'),
   path('memberships/', views.memberships, name='memberships'),
   path('contact-us/', views.contact_us, name='contact_us'),
   path('login/', views.login, name='login'),
   path('my-account/', views.my_account, name='my-account'),
   path('history/', views.history, name='history'),
   path('faq/', views.faq, name='faq'),
   path('st-george-home/', views.st_george_home, name='st_george')
]
