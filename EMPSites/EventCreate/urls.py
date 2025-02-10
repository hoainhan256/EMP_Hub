
from . import views
from django.urls import path
from .views import  create_event, event_detail

urlpatterns = [

    path("create_ev/", views.create_event, name="create_ev"), 
     
    
]