from django.db import models


class Location(models.Model):
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now=True)