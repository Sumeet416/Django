from django.http import HttpResponse 
from django.shortcuts import render

def home(Request):
    return render( Request , 'index.html')

def about(Request):
    return HttpResponse("Hello World, you are at about page")

def contact(Request):
    return HttpResponse("Hello World, you are at contact page")