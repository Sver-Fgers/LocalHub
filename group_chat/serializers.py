from rest_framework import serializers
from .models import Post, Comment
from users.models import UserProfile


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'created_on']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'created_on']


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    

    class Meta:
        model = UserProfile
        fields = ['user_id', 'name', 'bio', 'birth_date', 'location', 'picture']