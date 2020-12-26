
# Rest Framework
from rest_framework import serializers
# Models
from apps.heroe.models import Heroes


class HeroesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, allow_null=False)
    name = serializers.CharField(required=True, allow_null=True)
    description = serializers.CharField(required=True, allow_null=True)
    apparition = serializers.DateField(required=True, allow_null=True)

    class Meta:
        model = Heroes
        fields = ('id', 'name', 'description', 'apparition')
