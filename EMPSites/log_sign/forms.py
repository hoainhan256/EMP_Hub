# accounts/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nhập tên đăng nhập'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Nhập email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nhập mật khẩu'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nhập lại mật khẩu'}), required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Tên đăng nhập đã tồn tại!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email đã được sử dụng!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Mật khẩu và xác nhận mật khẩu không khớp!")
        return cleaned_data
