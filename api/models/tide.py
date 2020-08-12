from django.db import models
from .trip import Trip

class Tide(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  timestamp = models.CharField(null=True, max_length=100),
  datetime = models.DateField(null=True),
  height = models.CharField(null=True, max_length=100),
  state = models.CharField(null=True, max_length=100),
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

  def __str__(self):
      return f" at time {self.time_stamp}, it's {self.state}."
