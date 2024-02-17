from django.db import models


class User(models.Model):
    uuid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture = models.CharField(null=True, max_length=255, blank=True)

    def __str__(self):
        return self.name

