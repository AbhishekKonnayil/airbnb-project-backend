from django.urls import path
from .import views


urlpatterns = [
    path("", views.properties_list, name='property_list'),
    path('create/', views.create_property, name='create_property'),
    path('<uuid:pk>/', views.properties_detail, name='property_detail')
]
