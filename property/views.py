
from .models import Property
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import PropertiesListSerializer, PropertiesDetailsSerializer

from django.http import JsonResponse
from django.urls import reverse
from .forms import PropertyForm
from rest_framework import status


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


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_detail(request, pk):
    properties = Property.objects.get(pk=pk)
    serializer = PropertiesDetailsSerializer(properties, many=False)

    return JsonResponse(serializer.data)


@api_view(['POST', 'FILES'])
def create_property(request):
    try:
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            property = form.save(commit=False)
            property.landlord = request.user
            property.save()

            return JsonResponse({'success': True})
        else:
            print('error', form.errors, form.non_field_errors)

            return JsonResponse({'errors': form.errors.as_json()}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        raise e
