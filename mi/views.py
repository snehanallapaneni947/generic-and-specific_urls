from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def mumbai(request):
    return HttpResponse('<i>owner of mi is Ambani</i>')
def bumbra(request):
    return HttpResponse('<h1>Bumbra is very good bowler in mi</h1>')