from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class SkillSyncHubView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'

class ListCategoryView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'

class CreateCategoryView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'

class DeleteCategoryView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'


class CreateInstructorView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'


class InstructorListView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'


class InstructorDeleteView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'