from rest_framework import serializers
from account.models import CustomUser, Organistaion, Favorite


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['organisation_name'] = OrganisationSerializer(instance.organisation.name).data
        return ret


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organistaion
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

