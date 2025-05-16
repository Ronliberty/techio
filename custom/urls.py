from django.urls import path
from .views import RedirectAfterLoginView


app_name = 'custom'

urlpatterns = [

    path('redirect/', RedirectAfterLoginView.as_view(), name='redirect_after_login'),


]

