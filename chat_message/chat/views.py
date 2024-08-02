from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@api_view(['POST'])
def single_chat_add(request):
    if request.method == 'POST':
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def message_list(request):
    messages = ChatMessage.objects.all().order_by('-timestamp')
    return render(request, 'index.html', {'messages': messages})

@api_view(['DELETE'])
def delete_message(request, pk):
    try:
        message = ChatMessage.objects.get(pk=pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ChatMessage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

