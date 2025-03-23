from django.http import HttpResponse 
from django.shortcuts import render

def home(Request):
    return render( Request , 'index.html')

def about(Request):
    # return HttpResponse("Hello World, you are at about page")
    return render(Request , 'about.html')

def contact(Request):
    # return HttpResponse("Hello World, you are at contact page")
    return render(Request , 'contact.html')