from django.db import models
from django.conf import settings
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.utils import schema_context


class Tenant(TenantMixin):
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tenants")
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(help_text="Number of days the subscription lasts")
    features = models.JSONField(blank=True, null=True)  # List of included features

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'public'  # Ensures it is stored in the public schema

# ✅ Subscription Model (One per Tenant, in Public Schema)
class Subscription(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE, related_name="subscription")
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant.name} - {self.plan.name if self.plan else 'No Plan'}"

    class Meta:
        app_label = 'public'  # Ensures it is stored in the public schema

    def save(self, *args, **kwargs):
        with schema_context('public'):  # Ensure execution in the public schema
            super().save(*args, **kwargs)
