from . import views

from django.urls import path

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('services/', views.services, name='services'),
   path('memberships/', views.memberships, name='memberships'),
   path('contact-us/', views.contact_us, name='contact_us'),
   path('login/', views.user_login, name='login'),
   path('signup/', views.signup, name='signup'),
   path('forgot_password/', views.forgot_password, name='forgot_password'),
   path('password_reset_confirmation/', views.password_reset_confirmation, name='password_reset_confirmation'),
   path('reset_password/', views.reset_password, name='reset_password'),
   path('api/check_email_existence/', views.check_email_existence, name='check_email_existence'),
   path('my-account/', views.my_account, name='my-account'),
   path('history/', views.history, name='history'),
   path('faq/', views.faq, name='faq'),
   path('st-george-home/', views.st_george_home, name='st_george')
]
