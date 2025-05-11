from django.urls import path, include
from dj_rest_auth.jwt_auth import get_refresh_view
from .views import RegisterView_ , LoginView_

from dj_rest_auth.views import LogoutView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('register/', RegisterView_.as_view(), name='rest_register'),
    path('login/', LoginView_.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('accounts/', include('allauth.urls')),
]
