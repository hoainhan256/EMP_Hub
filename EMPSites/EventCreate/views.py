from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth import authenticate
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "home/home.html", {"event": event})



def create_event(request):
    # Kiểm tra người dùng đã đăng nhập chưa
    if not request.user.is_authenticated:
        messages.error(request, "Bạn cần đăng nhập trước khi tạo sự kiện.")
        return redirect("login")  # Chuyển hướng đến trang đăng nhập (nếu bạn có trang đăng nhập)
    
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect("/")  # Chuyển hướng đến trang chủ sau khi tạo sự kiện
    else:
        form = EventForm()
    
    return render(request, "EventCreate/create_ev.html", {"form": form})