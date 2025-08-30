from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import TimeStampedModel



class User(AbstractUser, TimeStampedModel):
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

class UserProfile(models.Model):
    # ONE USER HAS ONLY ONE PROFILE
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	birth_date=models.DateField(null=True, blank=True)
	location = models.CharField(max_length=100, blank=True, null=True)
	picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)

