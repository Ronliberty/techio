from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class EditingHubView(TemplateView):
    template_name = 'editing/editing-hub.html'