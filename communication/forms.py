from django.forms import ModelForm
from .models import Message, Audio
# Create the form class.
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_text']
        labels = {"message_text": "Mensaje para el paciente:"}

class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = ['audio']
        labels = {"audio": ".wav de prueba:"}