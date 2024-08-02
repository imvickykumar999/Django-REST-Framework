from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from django.contrib.auth.models import User
from django.shortcuts import render

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def single_chat_add(request):
    if request.method == 'POST':
        data = request.data.copy()
        serializer = ChatMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def chat_page(request):
    return render(request, 'index.html')
   
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def message_list(request):
    messages = ChatMessage.objects.filter(recipient=request.user).order_by('-timestamp')
    return Response(ChatMessageSerializer(messages, many=True).data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_message(request, pk):
    try:
        message = ChatMessage.objects.get(pk=pk, sender=request.user)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ChatMessage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

