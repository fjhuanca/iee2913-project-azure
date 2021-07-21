from django.urls import path
from .views import camera_page, dashboard_page, chart_test, messages_page

urlpatterns = [
    path('dashboard/', dashboard_page, name="dashboard"),
    path('camera/', camera_page, name="camera"),
    path('messages/', messages_page, name="messages"),
    path('temp_test/', chart_test, name="chart_test")
]