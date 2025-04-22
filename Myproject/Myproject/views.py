from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def blogs(request):
    return render(request, 'website/blogs.html')

def jobs(request):
    return render(request, 'website/jobs.html')



def home(Request):
    return render( Request , 'website/index.html')

def about(Request):
    # return HttpResponse("Hello World, you are at about page")
    return render(Request , 'website/about.html')

def blogs(Request):
    # return HttpResponse("Hello World, you are at contact page")
    return render(Request , 'website/blogs.html')

# def jobs(Request):
#     # return HttpResponse("Hello World, you are at jobs page")
#     return render(Request , 'website/jobs.html')

def application(Request):
    # return HttpResponse("Hello World, you are at application page")
    return render(Request , 'website/applicant_info.html')