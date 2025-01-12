from django.urls import path, include 
from chat.consumers import ChatConsumer
# the empty string routes to ChatConsumer, which manages the chat func 

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()), ]
