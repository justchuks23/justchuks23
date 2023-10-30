from django.shortcuts import render
from django.http import httpResponse

def hello(request):
    return render (request, 'hello.html')
     


