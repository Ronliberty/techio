from rest_framework import serializers
from .models import (
    ProjectTag, Project, SkillCategory, Skill,
    ContactInfo, SocialLink, LegalLink, HeroContent,
    ContactSubmission, PortfolioSection, PortfolioTemplate,
    UserPortfolio, PortfolioContent, ContentTag
)
from django.contrib.auth import get_user_model

User = get_user_model()


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tags = ProjectTagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    category = SkillCategorySerializer(read_only=True)

    class Meta:
        model = Skill
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class LegalLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalLink
        fields = '__all__'


class HeroContentSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = HeroContent
        fields = '__all__'


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'


class PortfolioSectionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PortfolioSection
        fields = '__all__'


class PortfolioTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioTemplate
        fields = '__all__'


class UserPortfolioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    template = serializers.PrimaryKeyRelatedField(queryset=PortfolioTemplate.objects.all())

    class Meta:
        model = UserPortfolio
        fields = '__all__'


class PortfolioContentSerializer(serializers.ModelSerializer):
    portfolio = serializers.PrimaryKeyRelatedField(queryset=UserPortfolio.objects.all())
    section = serializers.PrimaryKeyRelatedField(queryset=PortfolioSection.objects.all())

    class Meta:
        model = PortfolioContent
        fields = '__all__'


class ContentTagSerializer(serializers.ModelSerializer):
    section = serializers.PrimaryKeyRelatedField(queryset=PortfolioSection.objects.all())

    class Meta:
        model = ContentTag
        fields = '__all__'