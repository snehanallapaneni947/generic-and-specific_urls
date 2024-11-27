from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>virat is the captain of rcb</h1>')

def virat(request):
    return HttpResponse('<marquee>virat is very loyal to bangaluru</maequee>')