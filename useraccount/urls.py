from django.urls import path, include
from dj_rest_auth.jwt_auth import get_refresh_view
from .views import RegisterView_, LoginView_

from dj_rest_auth.views import LogoutView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

urlpatterns = [
    path('register/', RegisterView_.as_view(), name='rest_register'),
    path('login/', LoginView_.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('myreservations/', views.reservation_list, name='reservation_list'),
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),
    path('<uuid:pk>/', views.landlord_detail, name='landlord_detail')
]
