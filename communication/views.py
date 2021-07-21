from django.shortcuts import render, redirect
from .models import Messages, DrugRecords
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import datetime

# Create your views here.
def MessagesJsons(request):
    data = Messages.objects.all()
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
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        campo = datetime.datetime.today()
        hour, minute = body_data["time"].split(":")
        hour = int(hour)
        minute = int(minute)
        campo = campo.replace(hour=hour, minute=minute, second=0, microsecond=0)
        record = DrugRecords(time=campo)
        record.save()
        status = True
    return JsonResponse({"success": status}, safe=False)


