from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import TaskList, Task, Tag, Comment, Reminder
from .forms import TaskForm, TaskListForm, TagForm, CommentForm, ReminderForm


class ToDoHubView(TemplateView):
    template_name = 'todo/todo_hub.html'
class TaskListListView(LoginRequiredMixin, ListView):
    model = TaskList
    context_object_name = 'task_lists'

    def get_queryset(self):
        return TaskList.objects.filter(owner=self.request.user) | \
            TaskList.objects.filter(shared_with=self.request.user)


class TaskListCreateView(LoginRequiredMixin, CreateView):
    model = TaskList
    form_class = TaskListForm
    success_url = reverse_lazy('tasklist-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskListDetailView(LoginRequiredMixin, DetailView):
    model = TaskList
    context_object_name = 'task_list'



class TaskListUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskList
    form_class = TaskListForm
    success_url = reverse_lazy('tasklist-list')

    def get_queryset(self):
        return TaskList.objects.filter(owner=self.request.user)


class TaskListDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskList
    success_url = reverse_lazy('tasklist-list')

    def get_queryset(self):
        return TaskList.objects.filter(owner=self.request.user)


# Task Views
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


# Tag Views
class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    context_object_name = 'tags'



class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tag-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tag-list')

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tag-list')

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)


# Comment Views
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'tasks/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.task_id = self.kwargs['task_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['task_id']})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'tasks/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.task_id})

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)


# Reminder Views
class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tasks/reminder_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task_id = self.kwargs['task_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs['task_id']})


class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = 'tasks/reminder_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.task_id})

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)