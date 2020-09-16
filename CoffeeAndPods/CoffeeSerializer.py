from rest_framework import serializers
from .models import *


class CoffeeMachinesSerializer(serializers.ModelSerializer):
    product_type = serializers.StringRelatedField(many=False)

    class Meta:
        model = CoffeeMachines
        fields = (
            'sku', 'product_type', 'water_line_compatible',
        )


class CoffeePotSerializer(serializers.ModelSerializer):
    product_type = serializers.StringRelatedField(many=False)
    coffee_flavor = serializers.StringRelatedField(many=False)
    pack_size = serializers.StringRelatedField(many=False)

    class Meta:
        model = CoffeePot
        fields = (
            'sku', 'product_type', 'coffee_flavor', 'pack_size',
        )
