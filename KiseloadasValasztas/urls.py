from django.contrib import admin
from django.urls import include, path

from kiseloadas.views import indexview, feladatview, tanuloview



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('django.contrib.auth.urls'), name="index"),
    path('', indexview),
    path('feladatok', feladatview, name="feladats"),
    path('tanulok', tanuloview, name="tanulos"),
]
