from django.db import models

class ChatMessage(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

