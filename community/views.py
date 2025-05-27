
from django.urls import reverse_lazy
from django.shortcuts import render
from . models import ChatGroup
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, View
from .forms import GroupForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import Http404




class CreateGroupView(CreateView):
    model = ChatGroup
    form_class = GroupForm


class GroupListView(ListView):
    model = ChatGroup

class GroupEditView(UpdateView):
    model = ChatGroup
    form_class = GroupForm


class GroupDeleteView(DeleteView):
    model = ChatGroup
    success_url = reverse_lazy('')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class GroupLeaveView(View):

    def post(self, request, *args, **kwargs):
        chat_group = get_object_or_404(ChatGroup, pk=kwargs.get('pk'))

        if request.user not in chat_group.members.all():
            raise Http404("You are not a member of this group.")

        chat_group.members.remove(request.user)
        messages.success(request, 'You left the chat.')
        return redirect('home')