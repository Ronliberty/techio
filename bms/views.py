
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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class PostDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class NewsListView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = News
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class NewsDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = News
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class NewsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = News
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class ToolsListView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = Tool
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class ToolsDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Tool
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class ToolsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Tool
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class SkillsView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = Skill
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class SkillsDetailView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Skill
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class SkillsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Skill
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']


class ServiceListView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = Service
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class DeleteServiceView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Service

    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class DetailServiceView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = Service
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class RequestView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = ServiceRequest
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class DetailUserRequestView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = ServiceRequest
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class DeleteUserRequestView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = ServiceRequest
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

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
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class DetailResponseView(GroupRequiredMixin, LoginRequiredMixin,DetailView):
    model = ServiceResponse
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = ''


    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class ListResponseView(GroupRequiredMixin, LoginRequiredMixin,ListView):
    model = ServiceResponse
    context_object_name = ''
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

class DeleteResponseView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = ServiceResponse
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_template_names(self):
        user = self.request.user
        if user.groups.filter(name='manager').exists():
            return ['bms/manager/']
        elif user.groups.filter(name='agent').exists():
            return ['bms/agent/']
        return ['bms/default/']

