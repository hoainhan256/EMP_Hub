from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
from EventCreate.models import Event

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_events = models.ManyToManyField(Event, related_name='favorited_by')

    def add_to_favorites(self, event):
        self.favorite_events.add(event)