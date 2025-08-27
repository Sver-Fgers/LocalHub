from django.urls import path
from .views import PostListView

app_name = "chat"
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
]
