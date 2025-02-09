from django.shortcuts import render, get_object_or_404
from EventCreate .models import Event  # Import model Event
# Create your views here.
def Get_home(request):
    events = Event.objects.all().order_by("-date")
    return render(request,'home/home.html',{"events": events})  # Truyền vào template
    
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "home/event_detail.html", {"event": event})
def search(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        keys = Event.objects.filter(title__contains = searched)
    return render(request,'home/search.html',{"searched":searched,"keys":keys})