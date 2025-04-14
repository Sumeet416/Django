from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='Signup'),
    path('login/', views.SignIn, name='Login'),
]