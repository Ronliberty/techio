from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from allauth.account.models import EmailAddress
from .forms import CustomUserCreateForm, DeleteAccountForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from .models import CustomUser, Notify
from datetime import timedelta
from django.contrib.auth import logout  # Add this import
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseForbidden
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

class SettingsView(TemplateView):
    template_name = 'custom/settings.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Add user's email verification status
        email_address = EmailAddress.objects.filter(user=user, primary=True).first()
        context['email_verified'] = email_address.verified if email_address else False

        # Add password last changed date (you'll need to store this in your user model)
        # For now, we'll use the last login as a placeholder
        context['password_changed'] = user.last_login or user.date_joined

        return context

class DeleteAccountView(LoginRequiredMixin, FormView):
    template_name = 'custom/delete_account.html'
    form_class = DeleteAccountForm
    success_url = reverse_lazy('base:index')  # Change to your home URL

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user


        logout(self.request)


        user.delete()

        messages.success(self.request, 'Your account has been permanently deleted.')
        return super().form_valid(form)

    def _export_user_data(self, user):
        """
        Optional method to export user data before deletion
        (Implement according to your needs)
        """
        pass





class NotificationsView(TemplateView):
    template_name = 'custom/notify.html'
    model = Notify

class ProfileView(TemplateView):
    template_name = 'custom/profile.html'


class HelpView(TemplateView):
    template_name = 'custom/help.html'


class PoliciesView(TemplateView):
    template_name = 'custom/policy.html'








class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'custom/users.html'
    context_object_name = 'users'


    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        else:
            # Return a custom error page for non-HTMX requests
            return HttpResponseForbidden(
                render_to_string('custom_account/errors/htmx_only.html', {}, request=self.request)
            )

class UsersCreateView(CreateView):
    model = CustomUser
    template_name = 'custom/create_user.html'
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('custom_account:users-list')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        group = form.cleaned_data.get('group')
        if group:
            user.groups.add(group)

        # Check if the request is an HTMX request
        if self.request.headers.get('HX-Request'):
            # If it's an HTMX request, render the updated user list
            html = render_to_string(
                'custom_account/create.html',
                {'users': CustomUser.objects.all()},
                request=self.request
            )
            return HttpResponse(html)

        # Else, return the custom error page for non-HTMX requests
        else:
            # Return forbidden response for non-HTMX requests
            return HttpResponseForbidden(
                render_to_string('custom_account/errors/htmx_only.html', {}, request=self.request)
            )

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            html = render_to_string(self.template_name, {'form': form}, request=self.request)
            return HttpResponse(html, status=400)
        return super().form_invalid(form)