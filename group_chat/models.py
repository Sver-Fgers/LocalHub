from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    # user currently logged in
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)