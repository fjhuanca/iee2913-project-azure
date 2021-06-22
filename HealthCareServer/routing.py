from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from esp_comm import consumer
import django
django.setup()

websocket_urlPatter = [
    path('ws/ecg/', consumer.ECGConsumer.as_asgi()),
    path('ws/signs/', consumer.SignsConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket' :AuthMiddlewareStack(URLRouter(websocket_urlPatter))
    
})