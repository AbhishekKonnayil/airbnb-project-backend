from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializer import RegisterSerializer_, LoginSerializer_
from dj_rest_auth.views import LoginView
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User
from .serializers import UserDetailSerializer
from property.serializers import ReservationListSerializer

# Create your views here.


class RegisterView_(RegisterView):
    serializer_class = RegisterSerializer_


class LoginView_(LoginView):
    serializer_class = LoginSerializer_


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def reservation_list(request):
    reservations = request.user.reservations.all()
    serializer = ReservationListSerializer(reservations, many=True)
    print('user', request.user)

    return JsonResponse(serializer.data, safe=False)
