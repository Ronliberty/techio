from django.urls import path
from .views import CategoryCreateView, ShopHubView, CategoryListView, CategoryDetailView, CategoryDeleteView, CategoryUpdateView, ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView, OrderListView, OrderDetailView, AddressOrderListView, AddressDetailView, WishListView, WishDetailView, CouponCreateView, CouponListView, CouponUpdateView, CouponDetailView, CouponDeleteView, CartListView

app_name = 'shop'
urlpatterns = [
    path('shop0-hub/', ShopHubView.as_view(), name='shop-hub'),
    path('category/', CategoryCreateView.as_view(), name='category-create' ),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('delete/category/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),


#product
    path('product/', ProductListView.as_view(), name='prod-list'),
    path('create/product/', ProductCreateView.as_view(), name='prod-create'),
    path('update/product/<slug:slug>/', ProductUpdateView.as_view(), name='prod-update'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='prod-det'),
    path('delete/product/<slug:slug>/', ProductDeleteView.as_view(), name='prod-delete'),

#order
    path('order/', OrderListView.as_view(), name='order-List'),
    path('order/detail/<slug:slug>/', OrderDetailView.as_view(), name='order-detail'),

#   Address
    path('address/order/', AddressOrderListView.as_view(), name='order-address'),
    path('address/detail/<slug:slug>', AddressDetailView.as_view(), name='address-detail'),


#WishList
    path('wishlist/', WishListView.as_view(), name='wish-list'),
    path('wishlist/detail/', WishDetailView.as_view(), name='wish-detail'),


#Coupon
    path('coupon/create/', CouponCreateView.as_view(), name='coupon-create'),
    path('coupon/list/', CouponListView.as_view(), name='coupon-list'),
    path('coupon/update/', CouponUpdateView.as_view(), name='coupon-update'),
    path('coupon/detail/<slug:slug>/', CouponDetailView.as_view(), name='coupon-detail'),
    path('coupon/delete/<slug:slug>/', CouponDeleteView.as_view(), name='coupon-delete'),

#cart
    path('cart/list/', CartListView.as_view(), name='cart-list'),





]