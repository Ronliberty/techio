from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils.translation import gettext_lazy as _

import itertools
# Custom User Model with Extended Fields


User = settings.AUTH_USER_MODEL

class ProjectTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            for i in itertools.count(1):
                if not ProjectTag.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(ProjectTag)
    image = models.ImageField(upload_to='projects/')
    date = models.DateField()
    views = models.PositiveIntegerField(default=0)
    project_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            for i in itertools.count(1):
                if not Project.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.TextField(help_text="SVG path data or icon class")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            for i in itertools.count(1):
                if not SkillCategory.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    proficiency = models.PositiveIntegerField(help_text="Percentage value (0-100)")

    def __str__(self):
        return f"{self.name} ({self.category})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            for i in itertools.count(1):
                if not Skill.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_contact_info'
            )
        ]

    def __str__(self):
        return "Contact Information"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify("contact-info")
            self.slug = base_slug
            for i in itertools.count(1):
                if not ContactInfo.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('other', 'Other'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.TextField(help_text="SVG path data or icon class")
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_platform_display()} Profile"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.get_platform_display())
            self.slug = base_slug
            for i in itertools.count(1):
                if not SocialLink.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class LegalLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            for i in itertools.count(1):
                if not LegalLink.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class HeroContent(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    subtitle = models.CharField(max_length=255)
    # Image fields
    image = models.ImageField(
        upload_to='hero_images/',
        blank=True,
        null=True,
        help_text="Recommended size: 1200x800 pixels"
    )
    image_alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Alt text for accessibility"
    )
    # Existing fields
    cta_text = models.CharField(max_length=100)
    cta_link = models.URLField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hero', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hero Content"
        verbose_name_plural = "Hero Contents"
        constraints = [
            models.UniqueConstraint(
                fields=['is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_hero_content'
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.image_alt:
            self.image_alt = f"{self.name} hero image"
        super().save(*args, **kwargs)

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Message from {self.email}"

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a base slug from the name
            base_slug = slugify(self.name)
            self.slug = base_slug
            # Ensure uniqueness by appending a number if duplicates exist
            for i in itertools.count(1):
                if not ContactSubmission.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{base_slug}-{i}"
        super().save(*args, **kwargs)


class PortfolioSection(models.Model):
    SECTION_TYPES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('project', 'Project'),
        ('skill', 'Skill'),
        ('certification', 'Certification'),
        ('gallery', 'Gallery'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)


    title = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)


    custom_data = models.JSONField(default=dict, blank=True)


    related_sections = models.ManyToManyField('self', blank=True)

    class Meta:
        ordering = ['-start_date']



class PortfolioTemplate(models.Model):
    TEMPLATE_CHOICES = [
        ('developer', 'Developer Portfolio'),
        ('student', 'Student Portfolio'),
        ('artist', 'Artist Portfolio'),
    ]

    name = models.CharField(max_length=100)
    template_type = models.CharField(max_length=20, choices=TEMPLATE_CHOICES)
    base_css = models.TextField(blank=True)
    section_order = models.JSONField(default=list)

    # Allowed section types for this template
    allowed_sections = models.JSONField(default=list)


# User Portfolio Configuration
class UserPortfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    template = models.ForeignKey(PortfolioTemplate, on_delete=models.SET_NULL, null=True)
    sections = models.ManyToManyField(PortfolioSection, through='PortfolioContent')
    custom_css = models.TextField(blank=True)
    visibility = models.JSONField(default=dict)  # {'section_id': True/False}


# Through Model for Section Ordering/Configuration
class PortfolioContent(models.Model):
    portfolio = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE)
    section = models.ForeignKey(PortfolioSection, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    custom_style = models.JSONField(default=dict)

    class Meta:
        ordering = ['order']


# Social Media Integration
class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        unique_together = ('user', 'platform')


# Tagging System for Content Organization
class ContentTag(models.Model):
    TAG_CATEGORIES = [
        ('skill', 'Skill'),
        ('technology', 'Technology'),
        ('industry', 'Industry'),
    ]

    section = models.ForeignKey(PortfolioSection, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=TAG_CATEGORIES)
    value = models.CharField(max_length=100)