from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="home"),
    path("found", views.found, name="found"),
    path("lost", views.lost, name="lost"),
]