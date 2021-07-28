from django.db import models
from django.utils.timezone import now
import datetime
import time

def upload_root_gen(instance, filename):
    ts = time.time()
    sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H-%M-%S')
    return "audio/audio_"+sttime+".wav"

# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=now, editable=False)

class DrugRecord(models.Model):
    time = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)

class EvacuationRecord(models.Model):
    time = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)

class FoodRecord(models.Model):
    time = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)

class Audio(models.Model):
    created_date = models.DateTimeField(default=now, editable=False)
    audio = models.FileField(upload_to=upload_root_gen, blank=False)
    length = models.IntegerField(default=0)