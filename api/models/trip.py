from django.db import models

from .user import User

# Create your models here.
class Trip(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  launchDate = models.DateField(null=True)
  latitude = models.DateField(null=True)
  longitude = models.CharField(max_length=100)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Launching from latitude {self.latitude} and longitude {self.longitude} on '{self.launchDate}'."

  def as_dict(self):
    """Returns dictionary version of Trip models"""
    return {
        'id': self.id,
        'start date': self.launchDate,
        'latitude': self.latitude,
        'longitude': self.longitude
    }
