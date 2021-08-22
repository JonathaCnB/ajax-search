from django.db import models


class WebSeries(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name
