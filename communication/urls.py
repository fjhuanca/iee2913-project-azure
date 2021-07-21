from django.urls import path
from .views import CreateFoodRecord, MessagesJsons, CreateDrugRecord, CreateDrugRecord, CreateEvacuationRecord
from django.urls import path

urlpatterns = [
    path('messages/', MessagesJsons),
    path('drugs_record/', CreateDrugRecord),
    path('evacuation_record/', CreateEvacuationRecord),
    path('food_record/', CreateFoodRecord)

]