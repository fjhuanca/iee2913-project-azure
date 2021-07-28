from django.urls import path
from .views import audio_player, camera_page, dashboard_page, chart_test, messages_page,\
                   drugs_page, evacuation_page, food_page, audio_form_test, audio_player

urlpatterns = [
    path('dashboard/', dashboard_page, name="dashboard"),
    path('camera/', camera_page, name="camera"),
    path('messages/', messages_page, name="messages"),
    path('registro_medicamentos/', drugs_page, name="drugs"),    
    path('registro_comidas/', food_page, name="foods"),    
    path('registro_evacuaciones/', evacuation_page, name="evacuations"),
    path('temp_test/', chart_test, name="chart_test"),
    path('audio_form/', audio_form_test, name="audio_test"),
    path('audio_player', audio_player)
]