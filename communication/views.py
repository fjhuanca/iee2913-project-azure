from django.shortcuts import render, redirect
from .models import Message, DrugRecord, EvacuationRecord, FoodRecord, Audio
from .forms import AudioForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import datetime
import mutagen

# Create your views here.
def MessagesJsons(request):
    data = Message.objects.all()
    data = [model_to_dict(d) for d in data]
    n = len(data)
    dic = {"n": n}
    for i in range(n):
        dic[i] = data[i]["message_text"]
    return JsonResponse(dic, safe=False)

@csrf_exempt
def CreateDrugRecord(request):
    status = False
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            campo = datetime.datetime.today()
            hour, minute = body_data["time"].split(":")
            hour = int(hour)
            minute = int(minute)
            campo = campo.replace(hour=hour, minute=minute, second=0, microsecond=0)
            record = DrugRecord(time=campo)
            record.save()
            status = True
        except:
            status = False
    return JsonResponse({"success": status}, safe=False)

@csrf_exempt
def CreateFoodRecord(request):
    status = False
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            campo = datetime.datetime.today()
            hour, minute = body_data["time"].split(":")
            hour = int(hour)
            minute = int(minute)
            campo = campo.replace(hour=hour, minute=minute, second=0, microsecond=0)
            record = FoodRecord(time=campo)
            record.save()
            status = True
        except:
            status = False
    return JsonResponse({"success": status}, safe=False)

@csrf_exempt
def CreateEvacuationRecord(request):
    status = False
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            campo = datetime.datetime.today()
            hour, minute = body_data["time"].split(":")
            hour = int(hour)
            minute = int(minute)
            campo = campo.replace(hour=hour, minute=minute, second=0, microsecond=0)
            record = EvacuationRecord(time=campo)
            record.save()
            status = True
        except:
            status = False
    return JsonResponse({"success": status}, safe=False)


@csrf_exempt
def CreateVoiceNote(request):
    status = False
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        audio_form = AudioForm(request.POST, request.FILES)
        if audio_form.is_valid():
            audio = audio_form.save(commit=False)
            audio_info = mutagen.File(request.FILES['audio']).info
            audio.length = round(audio_info.length)
            audio.save()
            return redirect('messages')
    return JsonResponse({"success": status}, safe=False)