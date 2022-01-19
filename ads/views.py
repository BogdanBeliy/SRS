from rest_framework.response import Response

from ads.models import *
from ads.serializers import *
from rest_framework.views import APIView


class AllCategoriesView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ...




