from django.db import models
from django.contrib.auth.models import User
from EventCreate.models import Event  # Import model Event từ app CreateEvent
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Liên kết với sự kiện
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    role = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"
