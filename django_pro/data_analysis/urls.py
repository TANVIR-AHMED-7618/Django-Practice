

from django.urls import path
from . import views


urlpatterns = [
    path('', views.dataAnalysis),
    path('', views.da),
    
]