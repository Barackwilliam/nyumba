# from django.db import models
# from django.contrib.auth.models import User 


# # Create your models here.
# class ChatRoom(models.Model):
#     owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
#     customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Message(models.Model):
#     chat_room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.sender}->{self.receiver}: {self.content[50]}"
