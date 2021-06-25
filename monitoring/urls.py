from django.urls import path
from .views import camera_page, dashboard_page, chart_test

urlpatterns = [
    path('dashboard/', dashboard_page, name="dashboard"),
    path('camera/', camera_page, name="camera"),
    path('temp_test/', chart_test, name="chart_test")
]