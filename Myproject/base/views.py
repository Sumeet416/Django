from django.shortcuts import render

# Create your views here.

def SignUp(request):
    return render(request, 'registration/sign_up.html')

def SignIn(request):    
    return render(request, 'registration/login.html')