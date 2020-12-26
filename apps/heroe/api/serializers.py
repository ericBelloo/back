
# Rest Framework
from rest_framework import serializers
# Models
from apps.heroe.models import Heroes, Editorial


class HeroesListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=True)
    description = serializers.CharField(required=True, allow_null=True)
    apparition = serializers.DateField(required=True, allow_null=True)

    class Meta:
        model = Heroes
        fields = ('id', 'name', 'description', 'apparition')


class EditorialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=False)

    class Meta:
        model = Editorial
        fields = ('id', 'name')


class HeroeDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=True)
    description = serializers.CharField(required=True, allow_null=True)
    apparition = serializers.DateField(required=True, allow_null=True)
    editorial = EditorialSerializer(many=False, read_only=True)

    class Meta:
        model = Heroes
        fields = ('id', 'name', 'description', 'apparition', 'editorial')
