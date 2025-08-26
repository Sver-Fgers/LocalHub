# core/views.py
from django.shortcuts import render
from django.views import View

def homepage(request):
    return render(request, "login_home.html")

def in_progress(request):
    return render(request, "in_progress.html")

def news_list(request):
    return render(request, "news_list.html")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing.html")

# class InProgressView(View):
#     def get(self, request):
#         return render(request, "in_progress.html")

# class NewsListView(View):
#     def get(self, request):
#         return render(request, "news_list.html")
