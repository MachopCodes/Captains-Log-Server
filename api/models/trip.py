from django.db import models

from .user import User

# Create your models here.
class Trip(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  tripStart = models.DateField(null=True)
  tripEnd = models.DateField(null=True)
  location = models.CharField(max_length=100)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The trip to {self.location} starts on '{self.tripStart}' and ends on {self.tripEnd}."

  def as_dict(self):
    """Returns dictionary version of Trip models"""
    return {
        'id': self.id,
        'start date': self.tripStart,
        'end date': self.tripEnd,
        'location': self.location
    }
