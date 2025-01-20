from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('form_reg', views.form_reg, name="form_reg"),
   
]