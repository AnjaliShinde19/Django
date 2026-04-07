from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    message= "<h1>Hello, Welcome</h1>"
    return HttpResponse(message)

def gm_msg(request):
    msg1= "<h2 style='color:red;'>Good Morning!</h2>"
    return HttpResponse(msg1)

def ga_msg(request):
    msg2= "<h3>Good Afternoon!</h3>"
    return HttpResponse(msg2)

def ge_msg(request):
    msg3= "<h4>Good Evening!</h4>"
    return HttpResponse(msg3)