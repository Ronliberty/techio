from django.db import models
from django.utils import timezone
# Create your models here.
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