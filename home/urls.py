from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
   path('', views.home, name="home"),
   path('register', views.register, name="register"),
   path('logout', views.log_out, name="logout"),
   path('login', views.user_login, name="login"),
]