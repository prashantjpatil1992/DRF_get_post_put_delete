from rest_framework import serializers
from .models import Table


class Desrializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'