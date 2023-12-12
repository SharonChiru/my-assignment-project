
# Create your views here.
# sharon/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my homepage!")

def additional_page(request):
    return HttpResponse("This is my additional page.")
