from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):

    def __str__(self):
        return self.name

    name = models.TextField(max_length=50)
    users = models.ManyToManyField(User, null=True, blank=True)
