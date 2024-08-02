from django.urls import path
from .views import single_chat_add, message_list, delete_message

urlpatterns = [
    path('single-chat-add/', single_chat_add, name='single-chat-add'),
    path('messages/', message_list, name='message-list'),
    path('messages/<int:pk>/delete/', delete_message, name='delete-message'),
]

