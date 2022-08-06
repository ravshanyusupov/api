from rest_framework import serializers

from myapp.models import Api


class SerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'
