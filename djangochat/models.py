from datetime import datetime

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=254)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=254)
    room = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.value} | {self.user}"
