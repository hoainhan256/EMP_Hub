from django.contrib import admin
from .models import EventRegistration

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event','role', 'registered_at') 
    search_fields = ('name', 'email', 'phone') 
    list_filter = ('event', 'registered_at') 

admin.site.register(EventRegistration, EventRegistrationAdmin)