"""
URL configuration for localhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path("", include("core.urls")),  # LocalHub home page
    path("", include("landing.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # group chat
    path("chat/", include("group_chat.urls")),

    path("home/", views.homepage, name="homepage"),
    path("in-progress/", views.in_progress, name="in_progress"), 
    path("news/", views.news_list, name="news_list"),
    
    # # API routes
    # path("api/users/", include("users.urls")),
    # path("api/communities/", include("communities.urls")),
    # path("api/events/", include("events.urls")),
    # path("api/groups/", include("groups.urls")),
    # path("api/news/", include("news.urls")),
]

