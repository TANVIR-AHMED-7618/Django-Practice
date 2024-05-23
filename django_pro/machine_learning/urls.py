

from django.urls import path
from . import views 


urlpatterns = [
    path('mach/', views.machine),
]