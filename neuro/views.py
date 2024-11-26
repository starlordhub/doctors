from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Neuro(request):
    return HttpResponse('<h1>Department of Neuro</h1>Dr.Raju')