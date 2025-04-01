from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Tenant, Domain

# Make Tenant manageable from Django Admin
@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name", "owner", "active", "created_at")
    search_fields = ("name", "owner__username")

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("domain", "tenant", "is_primary")
    search_fields = ("domain",)
