from django.views.generic import (
    CreateView,
)

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import (
    EventCategory,
)

class EventCategoryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = EventCategory
    fields = ['name', 'code', 'image', 'priority', 'status']
    template_name = 'events/create_event_category.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)

def category_list(request):
    event_category = EventCategory.objects.all()
    return render(request, 'Events/event_category.html', {'event_category': event_category})


