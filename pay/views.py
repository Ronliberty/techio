from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, ListView
from .models import Analytics, Invoice
from django.urls import reverse_lazy
from .forms import AnalyticForm, InvoiceForm
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden
from shop.mixins import GroupRequiredMixin

class FinancialDashboardView(TemplateView):
    template_name = 'payment/financials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        context['page_title'] = 'Financial Dashboard'
        return context
    def render_to_response(self, context, **response_kwargs):
        if not self.request.headers.get('HX-Request'):
            return HttpResponseForbidden(
                render_to_string('custom_account/errors/htmx_only.html',
                                 context,
                                 request=self.request)
            )
        return super().render_to_response(context, **response_kwargs)


class InvoiceListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Invoice

    context_object_name = 'invoices'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['pay/managers/invoice-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['pay/merchant/invoice-list.html']
        return ['pay/default/invoice-list.html']

    def get_queryset(self):
        # Allow access to both managers and superusers
        if self.request.user.groups.filter(name='manager').exists() or self.request.user.is_superuser:
            return Invoice.objects.all()
        return Invoice.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.get_queryset()

        # Add user type to context if needed for template differences
        context['is_superuser'] = self.request.user.is_superuser
        context['is_manager'] = self.request.user.groups.filter(name='manager').exists()

        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.request.headers.get('HX-Request'):
            return HttpResponseForbidden(
                render_to_string('custom_account/errors/htmx_only.html',
                                 context,
                                 request=self.request)
            )
        return super().render_to_response(context, **response_kwargs)





class InvoiceDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Invoice

    context_object_name = 'invoices'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['pay/managers/invoice-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['pay/merchant/invoice-detail.html']
        return ['pay/default/invoice-detail.html']





class CreateInvoiceView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'pay/manager/invoice-form.html'

    success_url = reverse_lazy('pay:invoice-list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class InvoiceUpdateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'pay/manager/invoice-form.html'

    success_url = reverse_lazy('pay:invoice-list')

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InvoiceDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Invoice

    success_url = reverse_lazy('payment:invoice-manager')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['pay/managers/invoice-delete.html']
        elif user.groups.filter(name='merchant').exists():
            return ['pay/merchant/invoice-delete.html']
        return ['pay/default/invoice-delete.html']





class AnalyticsCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Analytics
    form_class = AnalyticForm
    template_name = 'pay/analytics-form.html'

    success_url = reverse_lazy('pay:analytics-list')
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)




class AnalyticsUpdateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Analytics
    form_class = AnalyticForm
    template_name = 'pay/analytics-form.html'

    success_url = reverse_lazy('pay:analytics-list')
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AnalyticsDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Analytics

    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'analytics'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['pay/managers/analytics-detail.html']
        elif user.groups.filter(name='merchant').exists():
            return ['pay/merchant/analytics-detail.html']
        return ['pay/default/analytics-detail.html']











class AnalyticsDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Analytics

    success_url = reverse_lazy('pay:analytics-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['pay/managers/analytics-delete.html']

        return ['pay/merchant/analytics-delete.html']





class AnalyticsListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Analytics

    context_object_name = 'analytics'


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['pay/managers/analytics-list.html']
        elif user.groups.filter(name='merchant').exists():
            return ['pay/merchant/analytics-list.html']
        return ['pay/default/analytics-list.html']