from django.contrib import admin
from django.urls import include, path

from kiseloadas.views import indexview, ujview



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls'), name="index"),
    path('', indexview),
    path('uj', ujview),
]
