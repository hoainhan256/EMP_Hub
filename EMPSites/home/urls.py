from django.urls import path
from home import views as home

urlpatterns = [
   path('',home.Get_home)
]