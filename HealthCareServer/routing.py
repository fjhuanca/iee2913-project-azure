from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from esp_comm import consumer
import django
django.setup()

websocket_urlPatter = [
    path('wss/ecg/', consumer.ECGConsumer.as_asgi()),
    path('wss/signs/', consumer.SignsConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket' :AuthMiddlewareStack(URLRouter(websocket_urlPatter))
    
})