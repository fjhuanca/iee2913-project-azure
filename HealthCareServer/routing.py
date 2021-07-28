from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from esp_comm import consumer
import django
django.setup()

websocket_urlPatter = [
    path('wss/receiver/ecg/', consumer.ECGConsumerReceiver.as_asgi()),
    path('wss/sender/ecg/', consumer.ECGConsumerSender.as_asgi()),
    path('wss/receiver/signs/', consumer.SignsConsumerReceiver.as_asgi()),
    path('wss/sender/signs/', consumer.SignsConsumerSender.as_asgi()),
    path('wss/receiver/cam/', consumer.CamConsumerReceiver.as_asgi()),    
    path('wss/sender/cam/', consumer.CamConsumerSender.as_asgi()),
    path('wss/receiver/led/', consumer.LedConsumerReceiver.as_asgi()),
    path('wss/sender/led/', consumer.LedConsumerSender.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket' :AuthMiddlewareStack(URLRouter(websocket_urlPatter))
    
})