# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("in-progress/", views.in_progress, name="in_progress"), 
    path("news/", views.news_list, name="news_list"),
]
