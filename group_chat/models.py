from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import your custom User and UserProfile
from users.models import User, UserProfile


# -----------------------------
# Posts
# -----------------------------
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_on}"

    def get_absolute_url(self):
        return reverse("chat:post-detail", kwargs={"pk": self.pk})


# -----------------------------
# Comments
# -----------------------------
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.pk}"

    def get_absolute_url(self):
        return reverse("chat:post-detail", kwargs={"pk": self.post.pk})


# -----------------------------
# Signals to create UserProfile automatically
# -----------------------------
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
