

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/', include('machine_learning.urls')),
    path('dl/', include('Deep_learning.urls')),
    path('da/', include('data_analysis.urls')),
    path('Blg/', include('Blogs.urls')),
]
