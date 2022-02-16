import json
from pprint import pprint

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Category
from ads.serializers import *
from rest_framework.views import APIView
from silk.profiling.profiler import silk_profile
from django.db import connection


class ShowAllCategoriesView(APIView):
    serializer_class = CategorySerializer

    @silk_profile(name="All cats with ads")
    def get(self, request, *args, **kwargs):
        categories = Category.objects.prefetch_related('sub_category')
        return Response(self.serializer_class(categories, many=True).data)


class AdvByCatView(APIView):
    serializer_class = AdvertisementSerializer

    @silk_profile(name='Adv by cat')
    def get(self, request, *args, **kwargs):
        adv = Advertisement.objects.filter(category_id=self.request.query_params.get('category')).select_related(
            'category')
        return Response(self.serializer_class(adv, many=True).data)


class AdvDetailView(APIView):
    serilizer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        adv = get_object_or_404(Advertisement, id=self.request.query_params.get('id'))
        pprint(self.request.META)
        return Response(self.serilizer_class(adv).data)
