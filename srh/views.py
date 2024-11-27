from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nkr(request):
    return HttpResponse('<b>nkr is a telugu guy</b> ')
def srhcaptain (request):
    return HttpResponse('<h1> cpatain of srh is a Australia player</h1>')
