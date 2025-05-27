
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.shortcuts import render
from .models import Post, News, Tool, Skill, Service, ServiceResponse, ServiceRequest
from .forms import PostForm, NewsForm, ToolForm, SkillForm, RequestForm, ResponseForm, ServiceForm
from shop.mixins import GroupRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



class  PostListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Post
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/post-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/post-list.html']
        return ['bms/default/post-list.html']


class PostDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/post-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/post-detail.html']
        return ['bms/default/post-detail.html']

class PostCreateView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/post-create.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/post-create.html']
        return ['bms/default/post-create.html']


class PostDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/post-delete.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/post-delete.html']
        return ['bms/default/post-delete.html']

class NewsListView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = News
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/news-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/news-list.html']
        return ['bms/default/news-list.html']


class NewsDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = News
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/news-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/news-detail.html']
        return ['bms/default/news-detail.html']

class NewsCreateView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/news-create.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/news-create.html']
        return ['bms/default/news-create.html']


class NewsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = News
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/news-delete.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/news-delete.html']
        return ['bms/default/news-delete.html']


class ToolsListView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = Tool
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/tools-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/tools-list.html']
        return ['bms/default/tools-list.html']


class ToolsDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Tool
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/tools-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/tools-detail.html']
        return ['bms/default/tools-detail.html']

class ToolsCreateView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = Tool
    form_class = ToolForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/tools-create.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/tools-create.html']
        return ['bms/default/tools-create.html']


class ToolsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Tool
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/tools-delete.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/tools-delete.html']
        return ['bms/default/tools-delete.html']


class SkillsView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = Skill
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/skill-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/skill-list.html']
        return ['bms/default/skill-list.html']

class SkillsDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Skill
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/skills-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/skills-detail.html']
        return ['bms/default/skills-detail.html']

class SkillsCreateView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/skill-create.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/skill-create.html']
        return ['bms/default/skill-create.html']


class SkillsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Skill
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/skill-delete.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/skill-delete.html']
        return ['bms/default/skill-delete.html']


class ServiceListView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = Service
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/service-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/service-list.html']
        return ['bms/default/service-list.html']

class CreateServiceView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/service-create.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/service-create.html']
        return ['bms/default/service-create.html']

class DeleteServiceView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Service

    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/delete-service.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/delete-service.html']
        return ['bms/default/delete-service.html']

class DetailServiceView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Service
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/service-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/service-detail.html']
        return ['bms/default/service-detail.html']

class CreateRequestServiceView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = ServiceRequest
    form_class = RequestForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/create-request.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/create-request.html']
        return ['bms/default/create-request.html']

class RequestView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = ServiceRequest
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/request-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/request-list.html']
        return ['bms/default/request-list.html']

class DetailUserRequestView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = ServiceRequest
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/request-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/request-detail.html']
        return ['bms/default/request-detail.html']

class DeleteUserRequestView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = ServiceRequest
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/request-delete.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/request-delete.html']
        return ['bms/default/request-delete.html']

class CreateResponseView(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = ServiceResponse

    form_class = ResponseForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/create-response.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/create-response.html']
        return ['bms/default/create-response.html']

class DetailResponseView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = ServiceResponse
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/response-detail.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/response-detail.html']
        return ['bms/default/response-detail.html']

class ListResponseView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = ServiceResponse
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/response-list.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/response-list.html']
        return ['bms/default/response-list.html']

class DeleteResponseView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = ServiceResponse
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/response-delete.html']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/response-delete.html']
        return ['bms/default/response-delete.html']

