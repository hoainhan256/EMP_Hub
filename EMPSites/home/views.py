from django.shortcuts import render

# Create your views here.
def Get_home(request):
    return render(request,'home/home.html')
    