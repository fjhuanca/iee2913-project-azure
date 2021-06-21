from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template.loader import get_template

# Create your views here.
def index_view(request):
    return redirect("dashboard")

