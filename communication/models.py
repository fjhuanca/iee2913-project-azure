from django.db import models
from django.utils.timezone import now
import datetime
import time
import os
from django.dispatch import receiver

def upload_root_gen(instance, filename):
    ts = time.time()
    sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H-%M-%S')
    return "audio/audio_"+sttime+".wav"

# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=40)
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


@receiver(models.signals.post_delete, sender=Audio)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Audio` object is deleted.
    """
    if instance.audio:
        if os.path.isfile(instance.audio.path):
            os.remove(instance.audio.path)

@receiver(models.signals.pre_save, sender=Audio)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Audio` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Audio.objects.get(pk=instance.pk).file
    except Audio.DoesNotExist:
        return False

    new_file = instance.audio
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)