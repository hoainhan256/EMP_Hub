from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_reg, name="form_reg"),
    path('submit-registration/', views.submit_registration, name="submit_registration"),
    
]