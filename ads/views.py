from rest_framework.response import Response

from ads.models import Category, SubCategory, Advertisement
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


class ShowAllAdvertisementView(APIView):
    serializer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.all()
        serializer = self.serializer_class(advertisement, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ...
