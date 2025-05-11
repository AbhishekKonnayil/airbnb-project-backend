
from .models import Property
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import PropertiesListSerializer
from django.http import JsonResponse
from django.urls import reverse


# Create your views here.

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):

    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)

    return JsonResponse({
        'data': serializer.data
    })


0
