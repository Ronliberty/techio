from django.db import models
from subs.models import Tenant



class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class POSType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class TenantService(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="services")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant.name} - {self.service_category.name}"

class TenantPOS(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="pos_types")
    pos_type = models.ForeignKey(POSType, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant.name} - {self.pos_type.name}"
