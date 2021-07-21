from django.shortcuts import render
from .models import Messages
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
def MessagesJsons(request):
    data = Messages.objects.all()
    data = [model_to_dict(d) for d in data]
    return JsonResponse(data, safe=False)


