from rest_framework import serializers
from .models import routemodel


class testserializer(serializers.ModelSerializer):
    class Meta:
        model=routemodel
        fields='__all__'