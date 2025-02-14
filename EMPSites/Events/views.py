from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib import messages
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


class EventCategoryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = EventCategory
    fields = ['name', 'code', 'image', 'priority', 'status']
    template_name = 'Events/edit_event_category.html'

def form_valid(self, form):
        messages.success(self.request, "Category updated successfully!")
        return super().form_valid(form)
def get_success_url(self):
        return reverse_lazy('event_category_list')

class EventCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = EventCategory
    template_name = 'Events/delete_event_category.html'  # Trang xác nhận xóa
    success_url = reverse_lazy('event_category_list')  # Điều hướng sau khi xóa
    success_message = "Category deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)