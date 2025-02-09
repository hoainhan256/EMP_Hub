from django.urls import path
from home import views as home
from .views import event_detail

urlpatterns = [
   path('',home.Get_home),
   
   path("event/<int:event_id>/", event_detail, name="event_detail"),  # Trang chi tiết sự kiện
   path('search',home.search,name ='search'),
]