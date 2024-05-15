from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def machine(request):
    return HttpResponse('Hello, Django!')


def deep_learning(request):
    return HttpResponse('This is my second view')
