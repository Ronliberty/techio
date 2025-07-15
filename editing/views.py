from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class EditingHubView(TemplateView):
    template_name = 'editing/editing-hub.html'

class EditingManagementView(TemplateView):
    template_name = 'editing/partials/manager_editing_tasks.html'

class ScriptsManagementView(TemplateView):
    template_name = 'editing/partials/manager_scripts_tasks.html'

class EditingServiceCreateView(LoginRequiredMixin, CreateView):
    model = EditingService
    fields = ['title', 'service_type', 'description', 'deadline', 'price', 'source_file']
    template_name = 'editservice_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('editservice_list')


class EditingServiceListView(ListView):
    model = EditingService
    template_name = 'editservice_list.html'


class EditingServiceDetailView(DetailView):
    model = EditingService
    template_name = 'editservice_detail.html'


class EditingServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = EditingService
    fields = ['title', 'description', 'deadline', 'status', 'price', 'final_deliverable']
    template_name = 'editservice_form.html'
    success_url = reverse_lazy('editservice_list')


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'deadline', 'file']
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description', 'deadline', 'file']
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


class EditorProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EditorProfile
    fields = ['bio', 'skills', 'portfolio_link', 'hourly_rate', 'available', 'max_projects']
    template_name = 'editorprofile_form.html'

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse('editorprofile_detail', kwargs={'pk': self.object.pk})


class EditorProfileDetailView(DetailView):
    model = EditorProfile
    template_name = 'editorprofile_detail.html'


class RevisionCreateView(LoginRequiredMixin, CreateView):
    model = EditingRevision
    fields = ['notes', 'revision_file']
    template_name = 'revision_form.html'

    def form_valid(self, form):
        form.instance.requested_by = self.request.user
        form.instance.editing_service = EditingService.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('editservice_detail', kwargs={'pk': self.kwargs['pk']})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = EditingComment
    fields = ['text', 'attachment']
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.editing_service = EditingService.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('editservice_detail', kwargs={'pk': self.kwargs['pk']})