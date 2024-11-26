from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Cardio(request):
    return HttpResponse('<h1>Department of Cardio</h1>Dr.Kishore')