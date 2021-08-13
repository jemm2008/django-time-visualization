
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('APP02_Visual_Tiempo.urls')),
    path('admin/', admin.site.urls),
]
