from django.urls import path
from .views import *


app_name = 'custom'

urlpatterns = [

    path('redirect/', RedirectAfterLoginView.as_view(), name='redirect_after_login'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
    path('settings/', SettingsView.as_view(), name='settings-menu'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('notify/', NotificationsView.as_view(), name='notify-settings'),
    path('profile/', ProfileView.as_view(), name='profile-settings'),
    path('help/', HelpView.as_view(), name='help-settings'),
    path('policies/', PoliciesView.as_view(), name='policy-settings'),


]

