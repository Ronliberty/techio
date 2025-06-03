from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404


# OurAgent Views
class AgentListView(ListView):
    model = OurAgent
    template_name = 'agent_list.html'
    context_object_name = 'agents'
    queryset = OurAgent.objects.filter(active=True)


class AgentDetailView(DetailView):
    model = OurAgent
    template_name = 'agent_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class AgentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = OurAgent
    fields = ['names', 'portfolio', 'email', 'social_links', 'phone_number', 'bio', 'active']
    template_name = 'agent_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('agent_detail', kwargs={'slug': self.object.slug})


class AgentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OurAgent
    fields = ['names', 'portfolio', 'email', 'social_links', 'phone_number', 'bio', 'active']
    template_name = 'agent_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('agent_detail', kwargs={'slug': self.object.slug})


# AgentImage Views
class AgentImageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AgentImage
    fields = ['image', 'title', 'caption']
    template_name = 'agentimage_form.html'

    def get_agent(self):
        return get_object_or_404(OurAgent, slug=self.kwargs['slug'])

    def form_valid(self, form):
        form.instance.expert = self.get_agent()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('agent_detail', kwargs={'slug': self.kwargs['slug']})


class AgentImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AgentImage
    template_name = 'agentimage_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('agent_detail', kwargs={'slug': self.object.expert.slug})


# Tickets Views
class TicketListView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Tickets.objects.all()
        return Tickets.objects.filter(owner=self.request.user)


class TicketDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Tickets
    template_name = 'ticket_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        ticket = self.get_object()
        return self.request.user.is_staff or ticket.owner == self.request.user


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Tickets
    fields = ['subject', 'description', 'priority']
    template_name = 'ticket_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'slug': self.object.slug})


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tickets
    fields = ['subject', 'description', 'priority', 'status', 'assigned_user', 'assigned_group']
    template_name = 'ticket_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.request.user.is_staff or self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'slug': self.object.slug})


# Information Views
class InformationListView(ListView):
    model = Information
    template_name = 'information_list.html'
    context_object_name = 'informations'


class InformationDetailView(DetailView):
    model = Information
    template_name = 'information_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class InformationCreateView(LoginRequiredMixin, CreateView):
    model = Information
    fields = ['name', 'description']
    template_name = 'information_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('information_detail', kwargs={'slug': self.object.slug})


class InformationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Information
    fields = ['name', 'description']
    template_name = 'information_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.request.user.is_staff or self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('information_detail', kwargs={'slug': self.object.slug})


class InformationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Information
    template_name = 'information_confirm_delete.html'
    success_url = reverse_lazy('information_list')

    def test_func(self):
        return self.request.user.is_staff or self.get_object().owner == self.request.user


# Information Media Views
class InformationImageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = InformationImage
    fields = ['image', 'caption']
    template_name = 'information_media_form.html'

    def get_information(self):
        return get_object_or_404(Information, slug=self.kwargs['slug'])

    def form_valid(self, form):
        form.instance.information = self.get_information()
        return super().form_valid(form)

    def test_func(self):
        info = self.get_information()
        return self.request.user.is_staff or info.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('information_detail', kwargs={'slug': self.kwargs['slug']})


class InformationVideoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = InformationVideo
    fields = ['video', 'title']
    template_name = 'information_media_form.html'

    def get_information(self):
        return get_object_or_404(Information, slug=self.kwargs['slug'])

    def form_valid(self, form):
        form.instance.information = self.get_information()
        return super().form_valid(form)

    def test_func(self):
        info = self.get_information()
        return self.request.user.is_staff or info.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('information_detail', kwargs={'slug': self.kwargs['slug']})


class InformationMediaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'information_media_confirm_delete.html'

    def get_object(self):
        model_map = {
            'image': InformationImage,
            'video': InformationVideo
        }
        model_class = model_map[self.kwargs['media_type']]
        return get_object_or_404(model_class, id=self.kwargs['pk'])

    def test_func(self):
        media = self.get_object()
        return self.request.user.is_staff or media.information.owner == self.request.user

    def get_success_url(self):
        media = self.get_object()
        return reverse_lazy('information_detail', kwargs={'slug': media.information.slug})