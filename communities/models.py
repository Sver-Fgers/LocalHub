# communities/models.py
from django.db import models
from core.models import TimestampedModel
from users.models import User

class Community(TimestampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="communities")

    def __str__(self):
        return self.name
