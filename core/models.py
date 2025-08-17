from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User with role field
class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("leader", "Leader"),
        ("user", "User"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    community = models.ForeignKey("Community", on_delete=models.CASCADE, null=True, blank=True, related_name="users")

    def __str__(self):
        return f"{self.username} ({self.role})"


class Community(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class NewsPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Group(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="groups")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserGroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "group")

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"
