from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Only email is required

    # Adding related_name to avoid conflicts with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Custom related name to avoid conflict
        blank=True
    )

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0]  # Auto-generate username from email
        super().save(*args, **kwargs)


class ProductionOrder(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('delayed', 'Delayed'),
    ]

    product = models.CharField(max_length=255)  # Simplified for static version
    quantity = models.PositiveIntegerField(default=1)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product}"



class Team(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_team')
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Team managed by {self.manager.username}"

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user who receives the notification
    message = models.TextField()  # The notification message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the notification was created
    is_read = models.BooleanField(default=False)  # Track if the notification has been read

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:30]}"



class Notify(models.Model):
    NOTIFICATION_TYPES = (
        ('update', 'Update'),
        ('alert', 'Alert'),
        ('info', 'Information'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, blank=True)
    action_url = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=50, default='fas fa-bell')

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.created_at}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.get_notification_type_display()}"

    @property
    def time_since(self):
        return timezone.now() - self.created_at