from django.test import TestCase
from django.urls import reverse
from EventCreate.models import Event
from EventReg.models import EventRegistration
from django.core import mail

from django.contrib.auth.models import User

class EventRegistrationTest(TestCase):
    def setUp(self):
        # Tạo một user
        self.organizer = User.objects.create(username="testuser")
        # Tạo một sự kiện 
        self.event = Event.objects.create(
            title="Test Event",
            description="A sample event for testing",
            date="2025-12-31 12:00:00",
            organizer=self.organizer 
        )

        self.registration_data = {
            "name": "Nguyen Van A",
            "email": "nguyenvana@example.com",
            "phone": "0123456789",
            "address": "123 Nguyen Trai, Hanoi",
            "role": "student",
            "event_id": self.event.id,
        }

    def test_form_reg_view(self):
        """Kiểm tra xem trang đăng ký có hiển thị không"""
        response = self.client.get(reverse("form_reg", args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Event Registration")
    
    def test_submit_registration_success(self):
        """Kiểm tra đăng ký thành công"""
        response = self.client.post(reverse("submit_registration"), self.registration_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(EventRegistration.objects.filter(email="nguyenvana@example.com").exists())
    
    def test_qr_generation(self):
        """Kiểm tra mã QR có được tạo ra không"""
        response = self.client.post(reverse("submit_registration"), self.registration_data)
        self.assertContains(response, "<img src=\"data:image/png;base64,")

