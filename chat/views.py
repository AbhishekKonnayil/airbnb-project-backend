from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


@api_view(['GET'])
@permission_classes([])
def conversation_list(request):
    serializer = ConversationListSerializer(
        request.user.conversations.all(), many=True)

    return JsonResponse(serializer.data, safe=False)
