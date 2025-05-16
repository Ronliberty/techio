from django.urls import path
from .views import  InvoiceListView, FinancialDashboardView, InvoiceDetailView, CreateInvoiceView, InvoiceDeleteView, AnalyticsCreateView, AnalyticsDetailView,  AnalyticsDeleteView, AnalyticsListView, AnalyticsUpdateView, InvoiceUpdateView


app_name = 'pay'

urlpatterns = [

    #invoice
    path('finances/', FinancialDashboardView.as_view(), name='finances'),

    path('invoice', InvoiceListView.as_view(), name='invoice-list'),

    path('create/invoice', CreateInvoiceView.as_view(), name='create-invoice'),
    path('update/invoice/<slug:slug>/', InvoiceUpdateView.as_view(), name='update-invoice'),

    path('invoice/detail/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),



    #analytics
    path('analytics/', AnalyticsListView.as_view(), name='analytics-list'),
    path('create/analytics/', AnalyticsCreateView.as_view(), name='create-analytic'),
    path('analytics/Update/<slug:slug>/', AnalyticsUpdateView.as_view(), name='update-analytic'),
    path('detail/analytic/<slug:slug>/', AnalyticsDetailView.as_view(), name='analytics-detail'),
    path('delete/<slug:slug>/', AnalyticsDeleteView.as_view(), name='analytic-delete'),




]