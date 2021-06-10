
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("hello world")
def greet(request,name):
    return HttpResponse(f"hello {name.capitalize()}")