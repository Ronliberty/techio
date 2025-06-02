from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

User = get_user_model()


class TaskList(models.Model):

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_lists')
    color = models.CharField(max_length=7, default='#4b6ea9', help_text="Hex color code")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shared_with = models.ManyToManyField(
        User,
        blank=True,
        related_name='shared_lists',
        help_text="Users who can view and modify this list"
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'name')

    def __str__(self):
        return f"{self.name} (by {self.owner.username})"

    @property
    def task_count(self):
        return self.tasks.count()

    @property
    def completed_count(self):
        return self.tasks.filter(status='completed').count()


class Task(models.Model):
    """Core task model"""
    PRIORITY_CHOICES = [
        (1, '⭐ Low'),
        (2, '⭐⭐ Medium'),
        (3, '⭐⭐⭐ High'),
        (4, '🔥 Urgent'),
    ]

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]

    # Core fields
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    # Ownership and relationships
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    task_list = models.ForeignKey(
        TaskList,
        on_delete=models.SET_NULL,
        related_name='tasks',
        blank=True,
        null=True
    )

    # Generic foreign key for platform integration
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    linked_object = GenericForeignKey('content_type', 'object_id')

    # Task management
    is_recurring = models.BooleanField(default=False)
    recurrence_rule = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="RRULE format (e.g., FREQ=DAILY;INTERVAL=1)"
    )
    estimated_minutes = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Estimated time to complete (minutes)"
    )

    # Visual and organization
    is_starred = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')

    class Meta:
        ordering = ['priority', 'due_date', '-created_at']
        indexes = [
            models.Index(fields=['due_date']),
            models.Index(fields=['status']),
            models.Index(fields=['priority']),
        ]

    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        if self.due_date and self.status != 'completed':
            return timezone.now() > self.due_date
        return False

    def save(self, *args, **kwargs):
        # Auto-complete timestamp
        if self.status == 'completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'completed' and self.completed_at:
            self.completed_at = None
        super().save(*args, **kwargs)


class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#6c757d')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tags',
        null=True,
        blank=True
    )
    is_global = models.BooleanField(
        default=False,
        help_text="Available to all users (admin only)"
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='task_attachments/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.task.title}"


class Reminder(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reminders')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remind_at = models.DateTimeField()
    notified = models.BooleanField(default=False)
    method = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('push', 'Push Notification')],
        default='push'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['remind_at']

    def __str__(self):
        return f"Reminder for {self.task.title} at {self.remind_at}"

    @property
    def is_active(self):
        return not self.notified and timezone.now() < self.remind_at


class ActivityLog(models.Model):

    ACTION_CHOICES = [
        ('create', 'Created'),
        ('update', 'Updated'),
        ('delete', 'Deleted'),
        ('status', 'Status Changed'),
        ('comment', 'Commented'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    details = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} {self.get_action_display()} task #{self.task.id}"