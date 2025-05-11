from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer



class RegisterSerializer_(RegisterSerializer):
    username = None
class LoginSerializer_(LoginSerializer):
    username=None