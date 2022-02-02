from django.urls import path
from account.views import CustomUserViewSet, OrganisationSettingsUpdate
from rest_framework import routers

urlpatterns = [
    path('organisation-settings/<int:pk>/', OrganisationSettingsUpdate.as_view({'get': 'retrieve', 'post': 'update'}), name='organisation_settings'),
    path('user-settings/<str:pk>/', CustomUserViewSet.as_view({'get': 'retrieve', 'post': 'update'}), name='user_settings'),
]
