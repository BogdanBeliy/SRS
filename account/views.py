from rest_framework.response import Response

from account.models import CustomUser
from account.serializers import CustomUserSerializer
from rest_framework.views import APIView


class UserView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.get(id=kwargs['user_id'])
        serializer = self.serializer_class(users).data
        return Response(serializer)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid()
        print(serializer.data)
        return Response('okey')


