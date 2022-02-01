from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import TemplateView
from account.models import CustomUser
from account.serializers import CustomUserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet


class CustomUserViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, id=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
