
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CreateUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
