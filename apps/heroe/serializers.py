
# Rest Framework
from rest_framework import serializers
# Models
from apps.heroe.models import Heroes, Editorial


class HeroesListSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=True)
    description = serializers.CharField(required=True, allow_null=True)
    apparition = serializers.DateField(required=True, allow_null=True)

    class Meta:
        model = Heroes
        fields = ('pk', 'name', 'description', 'apparition')


class EditorialSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=False)

    class Meta:
        model = Editorial
        fields = ('pk', 'name')


class HeroeDetailSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=False)
    description = serializers.CharField(required=True, allow_null=True)
    apparition = serializers.DateField(required=True, allow_null=True)
    editorial = EditorialSerializer(many=False, read_only=True)

    class Meta:
        model = Heroes
        fields = ('pk', 'name', 'description', 'apparition', 'editorial')
