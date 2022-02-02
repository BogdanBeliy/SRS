from rest_framework import serializers
from account.models import CustomUser, Organization, Favorite


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True)
    payment_status = serializers.CharField(read_only=True)
    pays = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['org'] = OrganisationSerializer(instance.organisation).data
        if instance.favorites.count() >= 1:
            ret['favorite'] = FavoriteSerializer(instance.favorites.all(), many=True).data
        else:
            ret['favorite'] = {}
        return ret


class OrganisationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    org_type = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Organization
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
