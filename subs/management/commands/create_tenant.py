from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from subs.models import Tenant, Domain

class Command(BaseCommand):
    help = "Create a new tenant with its domain"

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help="Tenant name", required=True)
        parser.add_argument('--domain', type=str, help="Domain for the tenant", required=True)
        parser.add_argument('--email', type=str, help="Email of the owner", required=True)

    def handle(self, *args, **kwargs):
        User = get_user_model()  # Get the custom user model

        # Get arguments
        name = kwargs['name']
        domain_name = kwargs['domain']
        owner_email = kwargs['email']

        # Get the user who will own the tenant
        try:
            owner = User.objects.get(email=owner_email)
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"User with email '{owner_email}' does not exist."))
            return

        # Create the tenant
        tenant = Tenant.objects.create(
            name=name,
            owner=owner,
            active=True
        )

        # Create the domain for the tenant
        domain = Domain.objects.create(
            domain=domain_name,
            tenant=tenant,
            is_primary=True
        )

        self.stdout.write(self.style.SUCCESS(f"✅ Tenant '{name}' with domain '{domain_name}' created successfully."))
