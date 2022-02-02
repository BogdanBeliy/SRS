from account.models import CustomUser, Organization
from account.serializers import CustomUserSerializer, OrganisationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class OrganisationSettingsUpdate(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganisationSerializer
