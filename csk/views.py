from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('cpatain of csk is ruturaj')

def vicecaptain(request):
    return HttpResponse('<h1>vicecaptain is dhoni</h1>')