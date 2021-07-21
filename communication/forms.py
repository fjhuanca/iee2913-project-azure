from django.forms import ModelForm
from .models import Messages
# Create the form class.
class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['message_text']
        labels = {"message_text": "Mensaje para el paciente:"}