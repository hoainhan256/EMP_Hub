from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from EventCreate.models import Event
from .models import Profile
def cart(request):
    context={}
    return render(request, "giaodich/cart.html",context)

def checkout(request):
    context={}
    return render(request, "giaodich/checkout.html",context)

@login_required
def cart(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    favorite_events = profile.favorite_events.all()  # Lấy danh sách sự kiện yêu thích của user

    context = {
        "favorite_events": favorite_events
    }
    return render(request, "giaodich/cart.html", context)
@login_required
def add_to_favorites(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    profile, created = Profile.objects.get_or_create(user=request.user)

    if event in profile.favorite_events.all():
        profile.favorite_events.remove(event)  # Bỏ yêu thích nếu đã có
    else:
        profile.favorite_events.add(event)  # Thêm vào danh sách yêu thích

    return redirect('cart')