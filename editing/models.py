from django.db import models
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    file = models.FileField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    accepted_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('available', 'available'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('on-hold', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    accepted = models.BooleanField(default=False)
    completed_on = models.DateTimeField(auto_now_add=True)  # Allow null if not yet completed

    def __str__(self):
        return f"{self.user.username} accepted {self.project.name}"


class EditingService(models.Model):
    SERVICE_TYPES = [
        ('VIDEO', 'Video Editing'),
        ('SCRIPT', 'Script Editing'),
        ('AUDIO', 'Audio Editing'),
        ('MULTI', 'Multimedia Editing'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editing_services')
    title = models.CharField(max_length=255)
    service_type = models.CharField(max_length=6, choices=SERVICE_TYPES)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('DRAFT', 'Draft'),
        ('SUBMITTED', 'Submitted'),
        ('ASSIGNED', 'Assigned to Editor'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('REVISION', 'Revision Requested'),
    ], default='DRAFT')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    assigned_editor = models.ForeignKey(
        'EditorProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_services'
    )
    source_file = models.FileField(upload_to='editing_source/', blank=True, null=True)
    final_deliverable = models.FileField(upload_to='editing_final/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_service_type_display()})"


class EditorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor_profile')
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    available = models.BooleanField(default=True)
    max_projects = models.PositiveIntegerField(default=3)
    current_projects = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} (Editor)"


class EditingRevision(models.Model):
    editing_service = models.ForeignKey(EditingService, on_delete=models.CASCADE, related_name='revisions')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    revision_file = models.FileField(upload_to='editing_revisions/', blank=True, null=True)

    def __str__(self):
        return f"Revision for {self.editing_service.title}"


class EditingComment(models.Model):
    editing_service = models.ForeignKey(EditingService, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='editing_comments/', blank=True, null=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.editing_service.title}"