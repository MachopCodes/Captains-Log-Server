from django.db import models

class CoorPair(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  city = models.CharField(null=True, max_length=100)
  state = models.CharField(null=True, max_length=100)
  key = models.CharField(null=True, max_length=100)
  lat = models.CharField(null=True, max_length=25)
  lng = models.CharField(null=True, max_length=25)

  def __str__(self):
    # This must return a string
    return f"{self.city}, {self.state} coordiantes are {self.lat} and {self.lng}." 

  def as_dict(self):
    """Returns dictionary version of Trip models"""
    return {
        'id': self.id,
        'city': self.city,
        'state': self.state,
        'iso': self.key,
        'latitude': self.lat,
        'longitude': self.lng
    }
