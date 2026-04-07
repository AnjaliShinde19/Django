from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h2>My World!</h2>")

def hi(request):
    return HttpResponse("<h2>My Ideas!</h2>")

def welcome(request):
    return HttpResponse("<h2>My Welcome!</h2>")