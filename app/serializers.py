from rest_framework import serializers
from .models import SumModel


class SumSerializer(serializers.ModelSerializer):

    class Meta:
        model = SumModel
        fields = '__all__'
