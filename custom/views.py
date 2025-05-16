from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View



from django.contrib.auth import get_user_model

User = get_user_model()

class RedirectAfterLoginView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user

        # Check user's group membership and redirect accordingly
        if user.groups.filter(name='default').exists():
            return redirect('dashboard:user_dashboard')
        elif user.groups.filter(name='manager').exists():
            return redirect('dashboard:manager-dashboard')
        elif user.groups.filter(name='agent').exists():
            return redirect('dashboard:agent-dashboard')
        elif user.is_superuser:
            return redirect('dashboard:super-dash')

        # Fallback
        return redirect('base:index')