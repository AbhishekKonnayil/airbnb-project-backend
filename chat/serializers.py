from .models import Conversation, ConversationMessage
from rest_framework import serializers
from useraccount.serializers import UserDetailSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    users = UserDetailSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at')
