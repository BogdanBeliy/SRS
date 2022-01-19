from django.shortcuts import render
from account.serializers import CustomUserSerializer
from rest_framework.views import APIView


class AllUserView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
