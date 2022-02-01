from rest_framework import serializers
from account.models import CustomUser, Organization, Favorite


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.organisation:
            ret['org'] = OrganisationSerializer(instance.organisation).data
        return ret




class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

