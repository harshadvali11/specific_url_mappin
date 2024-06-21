from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def kingkohli(request):
    return HttpResponse('<h1>Virat is the One Man Army of India and Rcb</h1>')


def captain(request):
    return HttpResponse('<h1>Faf is the Captain of Rcb</h1>')