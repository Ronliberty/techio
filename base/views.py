from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'base/index.html'


class CommunityView(TemplateView):
    template_name = 'base/community.html'


class InforView(TemplateView):
    template_name = 'base/infor.html'



class ErrorView(TemplateView):
    template_name = 'base/error.html'

class HelpCenterView(TemplateView):
    template_name = 'base/help-center.html'