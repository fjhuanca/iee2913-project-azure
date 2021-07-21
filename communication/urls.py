from django.urls import path
from .views import MessagesJsons
from django.urls import path

urlpatterns = [
    path('messages/', MessagesJsons),
]