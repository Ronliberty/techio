from django.urls import path, include
from . import api_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', api_views.ProductViewSet)
router.register(r'reviews', api_views.ProductReviewViewSet)
router.register(r'cart', api_views.CartViewSet, basename='cart')
router.register(r'cart-items', api_views.CartItemViewSet, basename='cartitem')
router.register(r'orders', api_views.OrderViewSet, basename='order')

order_item_router = DefaultRouter()
order_item_router.register(r'items', api_views.OrderItemViewSet, basename='orderitem')
urlpatterns = [

    path('', include(router.urls)),
    path('orders/<int:order_id>/', include(order_item_router.urls)),
]