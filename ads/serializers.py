
from ads.models import Category, SubCategory, Advertisement

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['sub_categories'] = SubCategorySerializer(instance.sub_category.all(), many=True).data
        return ret


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['name', ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['count_ads'] = instance.advertisement.all().count()
        return ret


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
