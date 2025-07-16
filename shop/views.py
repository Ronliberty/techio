from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView, View
from urllib3 import request

from .models import Category, Prod, Cart, Order, Coupon, Address, Wishlist
from .forms import CategoryForm, ProdForm
from .mixins import GroupRequiredMixin


class ShopHubView(TemplateView):
    template_name = 'shop/shop-hub.html'

class ProductManagementView(TemplateView):
    template_name = 'shop/partials/product_management.html'

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'shop/partials/merchant/cat-form.html'




class CategoryListView(ListView):
    model = Category
    template_name = 'shop/partials/merchants/cat-list.html'

    def render_to_response(self, context, **response_kwargs):
        if not self.request.headers.get('HX-Request'):
            return HttpResponseForbidden(
                render_to_string(
                    'custom/errors/htmx_only.html', context, request=self.request
                )
            )
        return super().render_to_response(context, **response_kwargs)
    


class CategoryDetailView(DetailView):
    model = Category

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/cat-detail.html']

        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchants/cat-detail.html']
        return ['shop/default/cat-detail.html']

    def test_func(self):
        return self.request.user.groups.filter( name__in=['manager', 'merchant', 'default']).exists()


class CategoryDeleteView(DeleteView):
    model = Category



class CategoryUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Category




class ProductListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Prod

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/prod-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchants/prod-list.html']
        return ['shop/default/prod-list.html']

    def test_func(self):
        return self.request.user.groups.filter(name__in=['manager', 'merchant', 'default']).exists()


class ProductCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Prod
    form_class = ProdForm
    template_name = 'shop/merchant/prod-form.html'





class ProductDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Prod

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/prod-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/prod-detail.html']
        return ['shop/default/prod-detail.html']


class ProductUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Prod

    def get_template_names(self):
        user = self.request.user

        if user.gropus.filter(name='manager').exists():
            return ['shop/managers/prod-form.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/prod-form.html']
        return ['shop/default/prod-form.html']


class ProductDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Prod

    def get_template_names(self):
        user = self.request.user

        if user.groups.filter(name='manager').exists():
            return ['shop/managers/prod-delete.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/prod-delete.html']
        return ['shop/default/prod-delete.html']

class CartListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Cart

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/cat-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/cat-list.html']

        return ['shop/default/cat-list.html']


class OrderListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Order

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/order-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/order-list.html']

        return ['shop/default/order-list.html']


class OrderDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Order

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/order-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/order-detail.html']

        return ['shop/default/order-detail.html']


class AddressOrderListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Address

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/address-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/address-list.html']

        return ['shop/default/address-list.html']


class AddressDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Address

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/address-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/address-detail.html']

        return ['shop/default/address-detail.html']

class WishListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Wishlist

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/wish-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/wish-list.html']

        return ['shop/default/wish-list.html']

class WishDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Wishlist

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/wish-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/wish-detail.html']

        return ['shop/default/wish-detail.html']


class CouponCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Coupon

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/coupon-form.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/coupon-form.html']

        return ['shop/default/coupon-form.html']


class CouponListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Coupon

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/coupon-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/coupon-list.html']

        return ['shop/default/coupon-list.html']


class CouponUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Coupon

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/coupon-form.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/coupon-form.html']

        return ['shop/default/coupon-form.html']


class CouponDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Coupon

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/coupon-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/coupon-detail.html']

        return ['shop/default/coupon-detail.html']


class CouponDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Coupon

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['shop/managers/coupon-delete.html']
        elif user.groups.filter(name='merchant').exists():
            return ['shop/merchant/coupon-delete.html']

        return ['shop/default/coupon-delete.html']

