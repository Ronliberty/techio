from rest_framework import serializers
from .models import Prod, ProductReviews, CartItem, Cart, Order, OrderItem



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    reviewer_name = serializers.SerializerMethodField()

    class Meta:
        model = ProductReviews
        fields = ['id', 'review_images', 'rating', 'reviews', 'status',
            'product', 'product_name', 'review_user', 'reviewer_name',
            'created_at']
        extra_kwargs = {
            'product': {'write_only': True},
            'review_user': {'write_only': True},
        }

    def get_reviewer_name(self, obj):
        if obj.review_user:
            return obj.review_user.get_full_name() or obj.review_user.username  #confirm this function later
        return "Anonymous"


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    subtotal = serializers.SerializerMethodField

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_price', 'quantity', 'subtotal']

        extra_kwargs = {
            'product': {'write_only': True},
        }

    def get_subtotal(self, obj):
        return obj.subtotal


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'session_key', 'created_at', 'items', 'total']
        extra_kwargs = {
            'user': {'write_only': True},
        }

        def  get_total(self, obj):
            return sum(item.subtotal() for item in obj.items.all())

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'user_email', 'order_date', 'status', 'total',
            'shipping_address', 'payment_method', 'payment_status', 'items'
        ]