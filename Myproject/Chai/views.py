from django.shortcuts import render
from .models import ChaiVarity
# Create your views here.
def chai(Request):
    chais = ChaiVarity.objects.all()
    return render(Request, 'chai/chai.html', {'chais':chais})