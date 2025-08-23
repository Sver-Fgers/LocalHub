# core/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")

def in_progress(request):
    return render(request, "in_progress.html")
