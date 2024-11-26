from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ent(request):
    return HttpResponse('<h1>Department of ENT</h1>Dr.Suresh')