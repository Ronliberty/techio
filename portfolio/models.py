from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Custom User Model with Extended Fields


User = settings.AUTH_USER_MODEL

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