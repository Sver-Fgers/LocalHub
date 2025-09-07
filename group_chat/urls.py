from django.urls import path
from .views import (
    PostListView, PostDetailView, 
    PostEditView, PostDeleteView, 
    CommentEditView, CommentDeleteView, 
    ProfileView, ProfileEditView,
    PostListCreateAPIView, PostDetailAPIView,
    CommentListCreateAPIView, CommentDetailAPIView,
    UserProfileListAPIView, UserProfileDetailAPIView
)

app_name = "chat"
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/edit/<int:pk>/', CommentEditView.as_view(), name='comment-edit'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),

        # API endpoints
    path('api/posts/', PostListCreateAPIView.as_view(), name='api-posts'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-detail'),

    path('api/comments/', CommentListCreateAPIView.as_view(), name='api-comments'),
    path('api/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='api-comment-detail'),

    path('api/profiles/', UserProfileListAPIView.as_view(), name='api-profiles'),
    path('api/profiles/<int:pk>/', UserProfileDetailAPIView.as_view(), name='api-profile-detail'),
]
