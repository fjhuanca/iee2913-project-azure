from communication.views import MessagesJsons
from django.contrib import admin

# Register your models here.
from .models import Messages, DrugRecords, EvacuationRecords, FoodRecords
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Messages)
admin.site.register(DrugRecords)
admin.site.register(EvacuationRecords)
admin.site.register(FoodRecords)
