from rest_framework import serializers
from .models import Project, UserProject, EditingService
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProjectSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'deadline',
            'file', 'file_url', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'file': {'write_only': True},
        }

    def get_file_url(self, obj):
        if obj.file:
            return self.context['request'].build_absolute_uri(obj.file.url)
        return None


class UserProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source='project',
        write_only=True
    )

    class Meta:
        model = UserProject
        fields = [
            'id', 'user', 'project', 'project_id',
            'status', 'accepted', 'accepted_at', 'completed_on'
        ]
        read_only_fields = ['user', 'accepted_at']


class EditingServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    assigned_editor = UserSerializer(read_only=True)
    source_file_url = serializers.SerializerMethodField()
    final_deliverable_url = serializers.SerializerMethodField()

    class Meta:
        model = EditingService
        fields = [
            'id', 'user', 'title', 'service_type', 'description',
            'deadline', 'status', 'price', 'assigned_editor',
            'source_file', 'source_file_url', 'final_deliverable',
            'final_deliverable_url', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'source_file': {'write_only': True},
            'final_deliverable': {'write_only': True},
        }

    def get_source_file_url(self, obj):
        if obj.source_file:
            return self.context['request'].build_absolute_uri(obj.source_file.url)
        return None

    def get_final_deliverable_url(self, obj):
        if obj.final_deliverable:
            return self.context['request'].build_absolute_uri(obj.final_deliverable.url)
        return None