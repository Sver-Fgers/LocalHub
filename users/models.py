from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import TimestampedModel


class User(AbstractUser, TimestampedModel):
    is_leader = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    @property
    def is_member(self):
        """User is considered a member if not admin or leader"""
        return not self.is_admin and not self.is_leader

    def __str__(self):
        roles = []
        if self.is_admin:
            roles.append("Admin")
        if self.is_leader:
            roles.append("Leader")
        if self.is_member:
            roles.append("Member")
        return f"{self.username} ({', '.join(roles)})"
