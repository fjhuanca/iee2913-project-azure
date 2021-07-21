from django.urls import path
from .views import MessagesJsons, CreateDrugRecord
from django.urls import path

urlpatterns = [
    path('messages/', MessagesJsons),
    # path('evacuation_record/'),
    # path('food_record/'),
    path('drugs_record/', CreateDrugRecord)

]