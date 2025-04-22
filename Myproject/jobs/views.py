from django.shortcuts import render
from . import views
# Create your views here.
def job(request):
    return render(request, 'jobs.html')
