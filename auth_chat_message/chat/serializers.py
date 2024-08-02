from rest_framework import serializers
from .models import ChatMessage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    recipient_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='recipient')

    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'recipient', 'recipient_id', 'message', 'timestamp']

