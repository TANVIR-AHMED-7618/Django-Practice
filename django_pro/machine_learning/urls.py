

from django.urls import path
from . import views 


urlpatterns = [
    path('', views.machine),
    path('ml/', views.ml),
]