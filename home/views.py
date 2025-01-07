from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import*
import json
# Create your views here.
def home(request):
    return render(request, 'home/app1.html')
def register(request):
    form= CreateUserForm()
    context={'form':form}
    if request.method=="POST":
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home/register.html',context)
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Chuyển hướng nếu đã đăng nhập

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Gọi hàm login từ Django
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect!')  # Thông báo lỗi

    context = {}
    return render(request, 'home/login.html', context)
def log_out(request):
    logout(request)
    return redirect ('login')