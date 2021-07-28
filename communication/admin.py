from communication.views import MessagesJsons
from django.contrib import admin

# Register your models here.
from .models import Message, DrugRecord, EvacuationRecord, FoodRecord, Audio
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Message)
admin.site.register(DrugRecord)
admin.site.register(EvacuationRecord)
admin.site.register(FoodRecord)
admin.site.register(Audio)
