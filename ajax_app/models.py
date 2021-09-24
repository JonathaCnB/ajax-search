from django.db import models


class WebSeries(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
