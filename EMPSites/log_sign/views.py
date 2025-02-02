# accounts/views.py

from django.shortcuts import render,redirect
import json
from django.http import HttpResponse,JsonResponse
from .models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def register(request):
    form = CreateUserForms
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid:
            form.save()
    context = {'form':form}
    return render(request, 'log_sign/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else: messages.info(request,'user or password inconrrect!')

    context = {}
    return render(request, 'log_sign/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')