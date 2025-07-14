from rest_framework import generics
from .models import Prod, ProductReviews, Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer,  ProductReviewSerializer, CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, status
User = get_user_model()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Prod.objects.all()
    serializer_class = ProductSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(review_user=self.request.user)


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(user=self.request.user)
        return Cart.objects.none()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # add logic here to create order items from cart
        serializer.save(user=self.request.user)

class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        order = get_object_or_404(Order, id=order_id, user=self.request.user)
        return OrderItem.objects.filter(order=order)