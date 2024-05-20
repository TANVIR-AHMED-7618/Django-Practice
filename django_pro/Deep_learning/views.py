from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deep(request):
    return HttpResponse('Wellcome to the Deep learning Apps')


def dl(request):
    return HttpResponse("Deep Learning is a brance of Computer Science")