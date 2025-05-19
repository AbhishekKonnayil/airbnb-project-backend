from rest_framework import serializers
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'name', 'avatar_url',)

    def get_name(self, obj):
        if obj.name:
            return obj.name
        return 'Undisclosed user'
