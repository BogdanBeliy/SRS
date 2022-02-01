from django.urls import path
from account.views import CustomUserViewSet
from rest_framework import routers

urlpatterns = [
    path('<str:pk>/', CustomUserViewSet.as_view({'get': 'retrieve'}))

]

