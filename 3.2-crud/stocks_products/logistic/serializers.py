from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            stock.positions.create(**position)
        return stock

    # def update(self, instance, validated_data):
    #     positions = validated_data.pop('positions')
    #     stock = super().update(instance, validated_data)
    #     for position in positions:
    #         pos_instance = position.pop('product')
    #         pos_instance.positions.update(**position)
    #     return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            product = position.pop('product') 
            StockProduct.objects.update_or_create(stock=stock.pk, product=product.pk, defaults=position)
        return stock