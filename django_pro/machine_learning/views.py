from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def machine(request):
    return render(request, 'machine_learning.html')

