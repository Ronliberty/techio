from django.urls import path

from .views import EditingHubView


app_name = 'editing'
urlpatterns = [
    path('edit-hub/', EditingHubView.as_view(), name='editing-hub'),
]