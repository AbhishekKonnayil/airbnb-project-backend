from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer, ConversationDetailSerializer, ConversationMessageSerializer
from rest_framework.decorators import api_view, permission_classes
from useraccount.models import User

# Create your views here.


@api_view(['GET'])
@permission_classes([])
def conversation_list(request):
    serializer = ConversationListSerializer(
        request.user.conversations.all(), many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def conversations_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)

    conversation_serializer = ConversationDetailSerializer(
        conversation, many=False)

    message_serializer = ConversationMessageSerializer(
        conversation.messages.all(), many=True)

    return JsonResponse({'conversation': conversation_serializer.data,
                         'messages': message_serializer.data}, safe=False)


@api_view(['GET'])
@permission_classes([])
def conversations_start(request, user_id):

    conversations = Conversation.objects.filter(
        users__in=[user_id]).filter(users__in=[request.user.id])

    if conversations.count() > 0:
        conversation = conversations.first()

        return JsonResponse({'success': True, 'conversation_id': conversation.id})

    else:
        user = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(user)

        return JsonResponse({'success': True, 'conversation_id': conversation.id})
