
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView, UpdateView
from django.shortcuts import render
from .models import Post, News, Tool, Skill, Service, ServiceResponse, ServiceRequest
from .forms import PostForm, NewsForm, ToolForm, SkillForm, RequestForm, ResponseForm, ServiceForm
from shop.mixins import GroupRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class BmsHubView(TemplateView):
    template_name = 'bms/default-hub.html'

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
    template_name = 'bms/manager/post-create.html'
    form_class = PostForm
    success_url = reverse_lazy('bms:tools-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class PostDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'bms/default/post-delete.html'
    success_url = reverse_lazy('bms:tools-detail')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



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
    template_name = 'bms/manager/news-create.html'
    success_url = reverse_lazy('bms:news-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class NewsUpdateView(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'bms/manager/news-update.html'
    success_url = reverse_lazy('bms:news-list')




class NewsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = News
    template_name = 'bms/manager/news-delete.html'
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'




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
    template_name = 'bms/manager/tools-create.html'
    form_class = ToolForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)




class ToolsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Tool
    template_name = 'tools-delete.html'
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'




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
    template_name = 'bms/manager/skill-create.html'
    form_class = SkillForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class SkillsDeleteView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Skill
    success_url = reverse_lazy('')
    template_name = 'bms/manager/skill-delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'




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
    template_name = 'bms/manager/service-create.html'
    form_class = ServiceForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteServiceView(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    model = Service
    template_name = 'bms/manager/delete-service.html'

    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



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
    template_name = 'bms/manager/create-response.html'
    form_class = ResponseForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


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
    template_name = 'bms/manager/response-delete.html'
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


