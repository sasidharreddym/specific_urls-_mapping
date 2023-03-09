from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ironman(request):
    return HttpResponse('<h1>Iron_Man is the richest avenger</h1>')

def rhodes(request):
    return HttpResponse('<h1>rhodes is the best friend of ironman</h1>')
