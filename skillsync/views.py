from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class SkillSyncHubView(TemplateView):
    template_name = 'skillsync/skill-sync-hub.html'
class EssaysManagementView(TemplateView):
    template_name = 'skillsync/partials/essay_management.html'

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


class AcademicServiceCreateView(LoginRequiredMixin, CreateView):
    model = AcademicService
    fields = ['service_type', 'title', 'description', 'deadline', 'pages', 'academic_level', 'price']
    template_name = 'academicservice_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('academicservice_detail', kwargs={'pk': self.object.pk})


class AcademicServiceListView(ListView):
    model = AcademicService
    template_name = 'academicservice_list.html'
    context_object_name = 'services'


class AcademicServiceDetailView(DetailView):
    model = AcademicService
    template_name = 'academicservice_detail.html'


class AcademicServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AcademicService
    fields = ['status', 'assigned_expert']
    template_name = 'academicservice_form.html'

    def test_func(self):
        return self.request.user.is_staff or self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse_lazy('academicservice_detail', kwargs={'pk': self.object.pk})


class OrderListView(LoginRequiredMixin, ListView):
    model = OrderAssign
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return OrderAssign.objects.filter(user=self.request.user)


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = OrderAssign
    template_name = 'order_detail.html'

    def test_func(self):
        return self.request.user == self.get_object().user
# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    fields = ['title', 'description', 'category', 'thumbnail', 'price', 'level', 'duration', 'featured']
    template_name = 'course_form.html'

    def test_func(self):
        return self.request.user.instructor_profile.approved

    def form_valid(self, form):
        form.instance.instructor = self.request.user.instructor_profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course_detail', kwargs={'slug': self.object.slug})


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['title', 'description', 'category', 'thumbnail', 'price', 'level', 'duration', 'featured']
    template_name = 'course_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.request.user == self.get_object().instructor.user

    def get_success_url(self):
        return reverse('course_detail', kwargs={'slug': self.object.slug})

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'course_delete.html'


class ModuleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Module
    fields = ['title', 'description', 'order']
    template_name = 'module_form.html'

    def get_course(self):
        return Course.objects.get(slug=self.kwargs['slug'])

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_course().instructor.user

    def get_success_url(self):
        return reverse('course_detail', kwargs={'slug': self.kwargs['slug']})


class VideoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Video
    fields = ['title', 'video_file', 'duration', 'thumbnail', 'description', 'transcript', 'is_preview', 'order']
    template_name = 'video_form.html'

    def get_module(self):
        return Module.objects.get(id=self.kwargs['module_id'])

    def form_valid(self, form):
        form.instance.module = self.get_module()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_module().course.instructor.user

    def get_success_url(self):
        return reverse('course_detail', kwargs={'slug': self.get_module().course.slug})
