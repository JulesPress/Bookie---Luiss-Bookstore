from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    Instagram = models.CharField(max_length=50, blank=True, null=True)
    Facebook = models.CharField(max_length=50, blank=True, null=True)
    Twitter = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)