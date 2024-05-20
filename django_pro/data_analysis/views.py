from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dataAnalysis(request):
    return HttpResponse("Welcome to Data Analysis!")


def da(request):
    return HttpResponse("Data Analysis is a major part of Computer Science")