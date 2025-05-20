
from .models import Property, Reservation
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import PropertiesListSerializer, PropertiesDetailsSerializer, ReservationListSerializer

from django.http import JsonResponse
from django.urls import reverse
from .forms import PropertyForm
from rest_framework import status
from useraccount.models import User
from rest_framework_simplejwt.tokens import AccessToken


# Create your views here.

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):

    try:
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer ')[1]
        token = AccessToken(token)
        user_id = token.payload['user_id']
        user = User.objects.get(pk=user_id)
    except Exception as e:
        user = None

    properties = Property.objects.all()
    favorites = []
    landlord_id = request.GET.get('landlord_id', "")
    if landlord_id:
        properties = properties.filter(landlord_id=landlord_id)

    if user:
        favorites = list(properties.filter(
            favorited=user).values_list('id', flat=True))
        # for property in properties:
        #     if user in property.favorited.all():
        # favorites.append(property.id)

    serializer = PropertiesListSerializer(properties, many=True)

    return JsonResponse({
        'data': serializer.data,
        'favorites': favorites
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_detail(request, pk):
    property = Property.objects.get(pk=pk)
    serializer = PropertiesDetailsSerializer(property, many=False)

    return JsonResponse(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def property_reservations(request, pk):
    property = Property.objects.get(pk=pk)
    reservation = property.reservations.all()
    serializer = ReservationListSerializer(reservation, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST', 'FILES'])
@permission_classes([])
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


@api_view(['POST'])
@permission_classes([])
def book_property(request, pk):
    try:
        start_date = request.POST.get('start_date', "")
        end_date = request.POST.get('end_date', "")
        number_of_nights = request.POST.get('number_of_nights', "")
        total_price = request.POST.get('total_price', "")
        guests = request.POST.get('guests', "")
        property = Property.objects.get(pk=pk)

        Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            number_of_nights=number_of_nights,
            total_price=total_price,
            guests=guests,
            created_by=request.user
        )
        return JsonResponse({'success': True})

    except Exception as e:
        print('error', e)
        return JsonResponse({'Success': False})


@api_view(['POST'])
@permission_classes([])
def toggle_favorite(request, pk):
    property = Property.objects.get(pk=pk)

    if request.user in property.favorited.all():
        property.favorited.remove(request.user)

        return JsonResponse({'is_favorite': False})
    else:
        property.favorited.add(request.user)

        return JsonResponse({'is_favorite': True})
