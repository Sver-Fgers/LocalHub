# events/models.py
from django.db import models
from core.models import TimestampedModel
from users.models import User
from communities.models import Community

class Event(TimestampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return self.title
