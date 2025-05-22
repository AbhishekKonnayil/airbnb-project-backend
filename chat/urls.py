from django.urls import path
from .import views

urlpatterns = [
    path('', views.conversation_list, name='conversation_list'),
    path('start/<uuid:user_id>/', views.conversations_start,
         name='conversations_start'),
    path('<uuid:pk>/', views.conversations_detail, name='conversations_detail')
]
