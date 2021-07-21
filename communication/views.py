from django.shortcuts import render
from .models import Messages
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
def MessagesJsons(request):
    data = Messages.objects.all()
    data = [model_to_dict(d) for d in data]
    n = len(data)
    dic = {"n": n}
    for i in range(n):
        dic[i] = data[i]["message_text"]
    return JsonResponse(dic, safe=False)


