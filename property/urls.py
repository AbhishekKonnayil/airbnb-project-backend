from django.urls import path
from .import views


urlpatterns = [
    path("", views.properties_list, name='property_list'),
    path('create/', views.create_property, name='create_property'),
    path('<uuid:pk>/', views.properties_detail, name='property_detail'),
    path('<uuid:pk>/book/', views.book_property, name='book_property'),
    path('<uuid:pk>/reservations/', views.property_reservations,
         name='property_reservations'),
    path('<uuid:pk>/toggle_favorite/', views.toggle_favorite,
         name='toggle_favorite'),

]
