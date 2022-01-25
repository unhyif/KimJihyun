from django.contrib import admin
from django.urls import path
from .views import *

app_name = "pirostagram"

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('like/', like, name="like"),
    path('comment/', comment, name="comment"),
    path('delete/', delete, name="delete")
]
