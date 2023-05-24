from django.contrib import admin
from django.urls import path, include
from .views import *
from ..blog import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<slug:post>', views.post_single, name="post_single")
]