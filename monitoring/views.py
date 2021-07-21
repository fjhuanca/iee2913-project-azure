from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from communication.forms import MessageForm
from communication.models import DrugRecords, Messages, FoodRecords, EvacuationRecords
from django.forms.models import model_to_dict
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
    message_data = Messages.objects.all()

    return render(request, "messages.html", {'form': message_form, 'message_data': message_data})

@login_required(login_url="login")
def drugs_page(request):
    data = DrugRecords.objects.all()
    return render(request, "registro_medicamentos.html", {'records_data': data})

@login_required(login_url="login")
def food_page(request):
    data = FoodRecords.objects.all()
    return render(request, "registro_comidas.html", {'records_data': data})

@login_required(login_url="login")
def evacuation_page(request):
    data = EvacuationRecords.objects.all()
    return render(request, "registro_evacuaciones.html", {'records_data': data})


def chart_test(request):
    return render(request, "chart_test.html")