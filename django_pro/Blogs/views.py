from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_blog(request):
    return render(request, 'blogs.html')
