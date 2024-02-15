from django.urls import path
from .views import *
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'ecomapp'
urlpatterns =[
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='ecomapp/login.html', authentication_form=LoginForm), name='login'),
]