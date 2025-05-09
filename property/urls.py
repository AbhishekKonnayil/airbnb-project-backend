from django.urls import path
from .import views


urlpatterns = [
    path("", views.properties_list, name='property_list'),
]
