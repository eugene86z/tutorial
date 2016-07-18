from rest_framework import serializers
from .models import propertyInfo


class propertyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = propertyInfo
        fields = ('address1','City','State','Zip')







