# accounts/views.py

from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from .models import*
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = CreateUserForms
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid:
            form.save()
    context = {'form':form}
    return render(request, 'log_sign/register.html', context)
def login(request):
    context = {}
    return render(request, 'log_sign/login.html', context)