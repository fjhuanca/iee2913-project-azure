from django.urls import path
from .views import CreateFoodRecord, MessagesJsons, CreateDrugRecord,\
                   CreateDrugRecord, CreateEvacuationRecord, CreateVoiceNote
from django.urls import path

urlpatterns = [
    path('messages/', MessagesJsons),
    path('drugs_record/', CreateDrugRecord),
    path('evacuation_record/', CreateEvacuationRecord),
    path('food_record/', CreateFoodRecord),
    path('voice_note/', CreateVoiceNote)

]