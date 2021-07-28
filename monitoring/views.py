from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from communication.forms import MessageForm, AudioForm
from communication.models import DrugRecord, Message, FoodRecord, EvacuationRecord, Audio
from django.forms.models import model_to_dict
import mutagen
from django.utils import timezone
import pytz
# Create your views here.

@login_required(login_url="login")
def dashboard_page(request):
    return render(request, "dashboard.html")

@login_required(login_url="login")
def camera_page(request):
    return render(request, "camera.html")

@login_required(login_url="login")
def messages_page(request):
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.save()
            return redirect('messages')
    else:
        message_form = MessageForm
    message_data = Message.objects.all()

    return render(request, "messages.html", {'form': message_form, 'message_data': message_data})

@login_required(login_url="login")
def drugs_page(request):
    data = DrugRecord.objects.all()
    return render(request, "registro_medicamentos.html", {'records_data': data})

@login_required(login_url="login")
def food_page(request):
    data = FoodRecord.objects.all()
    return render(request, "registro_comidas.html", {'records_data': data})

@login_required(login_url="login")
def evacuation_page(request):
    data = EvacuationRecord.objects.all()
    return render(request, "registro_evacuaciones.html", {'records_data': data})


def chart_test(request):
    return render(request, "chart_test.html")


def audio_form_test(request):
    if request.method == "POST":
        audio_form = AudioForm(request.POST, request.FILES)
        if audio_form.is_valid():
            audio = audio_form.save(commit=False)
            audio_info = mutagen.File(request.FILES['audio']).info
            audio.length = round(audio_info.length)
            audio.save()
            return redirect('messages')
    else:
        audio_form = AudioForm
    return render(request, "audio_test.html", {'form': audio_form})

def audio_player(request):
        audios = reversed(Audio.objects.all())
        print(timezone.get_current_timezone())
        base_url =  "{0}://{1}{2}".format(request.scheme, request.get_host(),"")
        lista = [AudioInTemplate(base_url, audio) for audio in audios]
        context = {'audio_list': lista}
        return render(request, "notas_de_voz.html", context)

class AudioInTemplate:
    def __init__(self, base_url, audio):
        minutes = audio.length // 60
        seconds = audio.length % 60
        self.time = audio.created_date
        self.url = base_url +audio.audio.url
        self.length = f"{minutes:02d}:{seconds:02d}"