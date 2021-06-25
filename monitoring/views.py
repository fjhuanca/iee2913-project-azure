from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def dashboard_page(request):
    return render(request, "dashboard.html")

@login_required(login_url="login")
def camera_page(request):
    return render(request, "camera.html")

def chart_test(request):
    return render(request, "chart_test.html")