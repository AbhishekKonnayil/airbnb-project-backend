from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializer import RegisterSerializer_, LoginSerializer_
from dj_rest_auth.views import LoginView

# Create your views here.


class RegisterView_(RegisterView):
    serializer_class = RegisterSerializer_


class LoginView_(LoginView):
    serializer_class = LoginSerializer_
