from django.db import models

from .user import User

# Create your models here.
class Trip(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  ripe = models.BooleanField()
  color = models.CharField(max_length=100)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The trip named '{self.name}' is {self.color} in color. It is {self.ripe} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Trip models"""
    return {
        'id': self.id,
        'name': self.name,
        'ripe': self.ripe,
        'color': self.color
    }
