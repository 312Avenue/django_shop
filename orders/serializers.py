from rest_framework import serializers

from .models import Order, OrderItems


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'create_at', 'address', 'items', 'total_sum']

    def create(self, validated_data):
        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data)
        total_sum = 0
        for item in items:
            OrderItems.objects.create(order=order, product=item['product'], quantity=item['quantity'])
            total_sum += item['product'].price * item['quantity']
        order.total_sum = total_sum
        order.save()
        return order