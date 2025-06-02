from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    bio = models.TextField()
    expertise = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='instructors/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    approved = models.BooleanField(default=False)  # Admin approval status

    def __str__(self):
        return f"{self.user.username} (Instructor)"

class AcademicService(models.Model):
    SERVICE_TYPES = [
        ('ASSIGN', 'Assignment Help'),
        ('DISS', 'Dissertation'),
        ('ESSAY', 'Essay Writing'),
        ('RES', 'Research Paper'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='academic_services')
    service_type = models.CharField(max_length=6, choices=SERVICE_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    pages = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    academic_level = models.CharField(max_length=50, choices=[
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('MA', 'Masters'),
        ('PHD', 'PhD'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('ASSIGNED', 'Assigned to Expert'),
        ('COMPLETE', 'Completed'),
        ('REVISION', 'Revision Requested'),
    ], default='PENDING')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    assigned_expert = models.ForeignKey(
        InstructorProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_services'
    )

    def __str__(self):
        return f"{self.get_service_type_display()} - {self.title}"

class OrderAssign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('COMPLETE', 'Completed'),
        ('FAILED', 'Failed'),
    ], default='PENDING')
    payment_id = models.CharField(max_length=100, blank=True, null=True)

    # Generic foreign key approach (could use Polymorphic instead)
    service = models.ForeignKey(AcademicService, null=True, blank=True, on_delete=models.SET_NULL)
    course_subscription = models.ForeignKey('Subscription', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"




class Course(models.Model):
    LEVEL_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField()
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default='B')
    duration = models.PositiveIntegerField(help_text="Total course duration in minutes", default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Video(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='course_videos/')

    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    order = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    transcript = models.TextField(blank=True, null=True)
    is_preview = models.BooleanField(default=False)  # Free preview video

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    last_play_time = models.FloatField(default=0.0, help_text="Last playback position in seconds")

    class Meta:
        verbose_name_plural = "User Progress"
        unique_together = ('user', 'video')

    def __str__(self):
        status = "Completed" if self.completed else "In Progress"
        return f"{self.user.username} - {self.video.title} ({status})"


class CourseReview(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.course.title} - {self.get_rating_display()}"