from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def captainamerica(request):
    return HttpResponse('<h1>Captain_America is the first avenger</h1>')

def thor(request):
    return HttpResponse('<h1>thor is the god of thunder</h1>')