from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializer import RegisterSerializer_
# Create your views here.


class RegisterView_(RegisterView):
    serializer_class = RegisterSerializer_
