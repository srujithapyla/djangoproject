from .models import *
from rest_framework import serializers

class sampleserializers(serializers.ModelSerializer):
    class Meta:
        model=routemodel1
        fields='__all__'