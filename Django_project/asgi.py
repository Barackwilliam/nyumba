from channels.routing import ProtocolTypeRouter, URLRouter 
from chat import routing
from channels.auth import AuthMiddlewareStack 
import os
from django.urls import path
from Myapp import consumers
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_project.settings')
application = ProtocolTypeRouter(     
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(             
            URLRouter(
                routing.websocket_urlpatterns            
                 )
        )
    }
)
