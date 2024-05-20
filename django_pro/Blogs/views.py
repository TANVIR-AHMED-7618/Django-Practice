from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_blog(request):
    return HttpResponse('Welcom to my first Blog.')


def second_blog(request):
    return HttpResponse("This is my second Blog. Welcome back again!")