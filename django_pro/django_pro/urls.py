

from django.contrib import admin
from django.urls import path
from machine_learning.views import machine
from machine_learning.views import deep_learning
from Blogs.views import first_blog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', machine),
    path('deep/', deep_learning),
    path('fb/',first_blog),
]
