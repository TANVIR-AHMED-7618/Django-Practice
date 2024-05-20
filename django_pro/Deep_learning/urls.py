

from django.urls import path
from . import views


urlpatterns = [
    path('', views.deep),
    path('',views.dl),
    
]