# serializers.py
from rest_framework import serializers
from .models import Post, News, Tool, Skill, Service
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'description', 'country',
            'link', 'image', 'image_url', 'status',
            'created_by', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'image': {'write_only': True},
            'slug': {'read_only': True},
        }

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None


class NewsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = [
            'id', 'headline', 'slug', 'content', 'country',
            'created_by', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'slug': {'read_only': True},
        }


class ToolSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Tool
        fields = [
            'id', 'name', 'slug', 'description', 'link',
            'country', 'image', 'image_url', 'created_by',
            'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'image': {'write_only': True},
            'slug': {'read_only': True},
        }

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None


class SkillSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Skill
        fields = [
            'id', 'name', 'slug', 'description', 'country',
            'created_by', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'slug': {'read_only': True},
        }


class ServiceSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'description', 'sample_website',
            'country', 'created_by', 'created_at', 'updated_at',
            'is_deleted'
        ]
        extra_kwargs = {
            'slug': {'read_only': True},
        }