# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
from .formsLogin import LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu đã xác thực
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Tạo người dùng mới
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
            messages.success(request, "Đăng ký thành công!") # Chuyển hướng đến trang đăng nhập hoặc trang khác
        else:
            messages.error(request, "Đã có lỗi xảy ra, vui lòng kiểm tra lại thông tin!")
    else:
        form = RegistrationForm()

    return render(request, 'log_sign/register.html', {'form': form})

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"dang nhap thanh cong") # Redirect to home page
        else:
             messages.error(request,"login fail")
    else:   
        form = AuthenticationForm()
    return render(request, 'log_sign/login.html', {'form': form})