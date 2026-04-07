from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def get_time(request):
    date = datetime.datetime.now()
    hr = date.strftime('%I')
    min = date.strftime('%M')
    sec = date.strftime('%S')
    res = "<h1>"+hr+ ":"+ min+":"+sec+"</h1>"
    return HttpResponse(res)
