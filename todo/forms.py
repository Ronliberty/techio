from django import forms
from .models import Task, TaskList, Tag, Comment, Reminder


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'due_date', 'priority', 'status',
            'task_list', 'is_recurring', 'recurrence_rule',
            'estimated_minutes', 'is_starred', 'tags'
        ]
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['task_list'].queryset = TaskList.objects.filter(
                models.Q(owner=user) |
                models.Q(shared_with=user)
            ).distinct()
            self.fields['tags'].queryset = Tag.objects.filter(
                models.Q(owner=user) |
                models.Q(is_global=True)
            ).distinct()


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name', 'color', 'shared_with']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shared_with'].queryset = self.fields['shared_with'].queryset.exclude(
            id=self.instance.owner_id
        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color', 'is_global']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'attachment']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['remind_at', 'method']
        widgets = {
            'remind_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }