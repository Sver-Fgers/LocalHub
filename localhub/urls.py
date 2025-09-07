from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", include("landing.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),

    # user API (signup, etc.)
    path("users/api/", include("users.urls")),  

    # group chat (web + API)
    path("chat/", include("group_chat.urls")),

    # normal template routes
    path("home/", views.homepage, name="homepage"),
    path("in-progress/", views.in_progress, name="in_progress"), 
    path("news/", views.news_list, name="news_list"),
    
    # JWT Authentication endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
