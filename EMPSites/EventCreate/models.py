from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', default='/path/to/default_image.jpg')
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.event.title} - {self.price}"
