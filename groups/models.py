# groups/models.py
from django.db import models
from core.models import TimeStampedModel
from users.models import User
from communities.models import Community

class Group(TimeStampedModel):
    name = models.CharField(max_length=255)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="groups")

    def __str__(self):
        return self.name

class UserGroupMembership(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[("member", "Member"), ("leader", "Leader")])

    class Meta:
        unique_together = ("user", "group")

    def __str__(self):
        return f"{self.user} in {self.group}"
