from django.conf import settings
from django.db import models


class Events(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.ForeignKey(
        "eventapp.Locations",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="events_location",
    )


class Locations(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    address1 = models.CharField(max_length=256,)
    address2 = models.CharField(max_length=256,)
    city = models.CharField(max_length=128,)
    state = models.CharField(max_length=2,)
    zip = models.CharField(max_length=5,)


# Create your models here.
