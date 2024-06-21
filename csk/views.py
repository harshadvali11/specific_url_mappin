from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msdhoni(request):
    return HttpResponse('<h1>Msd is a Best Wk batsman</h1>')

def captain(request):
    return HttpResponse('<h1>Ruturaj is the New Captain of CSk</h1>')