from django.db import models


class User(models.Model):
    uuid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_picture = models.FileField(upload_to='profile_pictures/', null=True, blank=True)

