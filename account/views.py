from rest_framework.response import Response

from account.models import CustomUser
from account.serializers import CustomUserSerializer
from rest_framework.views import APIView


class AllUserView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = self.serializer_class(users, many=True).data
        return Response(serializer)