# news/models.py
from django.db import models
from core.models import TimeStampedModel
from users.models import User
from communities.models import Community

class NewsPost(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="news_posts")

    def __str__(self):
        return self.title
