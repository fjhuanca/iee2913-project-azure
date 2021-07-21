from django.db import models
from django.utils.timezone import now


# Create your models here.
class Messages(models.Model):
    message_text = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=now, editable=False)

class DrugRecords(models.Model):
    time = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)

class EvacuationRecords(models.Model):
    time = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)

class FoodRecords(models.Model):
    time = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)