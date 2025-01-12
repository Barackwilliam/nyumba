# consumers.py
from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth.models import User
from .models import ChatMessage

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        time = text_data_json['time']

        # Assuming you are sending messages between authenticated users
        sender = User.objects.get(username=username)
        receiver = User.objects.exclude(username=username).first()  # This example assumes a single receiver

        # Save the message to the database
        ChatMessage.objects.create(
            sender=sender,
            receiver=receiver,
            message=message,
            timestamp=time
        )

        # Broadcast the message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'time': time
        }))


# class NotificationConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass 

#     def receive(self,text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         # Tuma message kwa User
#         self.send(text_data = json.dumps({
#             'message':message
#         }))

