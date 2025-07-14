from rest_framework import serializers
from .models import (
    Category, InstructorProfile, AcademicService, OrderAssign,
    Course, Module, Video, Subscription, UserProgress, CourseReview
)
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class InstructorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = InstructorProfile
        fields = [
            'id', 'user', 'bio', 'expertise', 'profile_picture',
            'profile_picture_url', 'website', 'approved'
        ]
        extra_kwargs = {
            'profile_picture': {'write_only': True},
        }

    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None

class AcademicServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    assigned_expert = InstructorProfileSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    service_type_display = serializers.CharField(source='get_service_type_display', read_only=True)
    academic_level_display = serializers.CharField(source='get_academic_level_display', read_only=True)

    class Meta:
        model = AcademicService
        fields = [
            'id', 'user', 'service_type', 'service_type_display', 'title',
            'description', 'deadline', 'pages', 'academic_level',
            'academic_level_display', 'created_at', 'status', 'status_display',
            'price', 'assigned_expert'
        ]

class OrderAssignSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    service = AcademicServiceSerializer(read_only=True)
    payment_status_display = serializers.CharField(source='get_payment_status_display', read_only=True)

    class Meta:
        model = OrderAssign
        fields = [
            'id', 'user', 'created_at', 'total_amount',
            'payment_status', 'payment_status_display', 'payment_id',
            'service', 'course_subscription'
        ]

class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorProfileSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    thumbnail_url = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'description', 'instructor',
            'category', 'created_at', 'updated_at', 'thumbnail',
            'thumbnail_url', 'price', 'level', 'level_display',
            'duration', 'featured', 'average_rating'
        ]
        extra_kwargs = {
            'thumbnail': {'write_only': True},
        }

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)
        return None

    #def get_average_rating(self, obj):
       # return obj.reviews.aggregate(models.Avg('rating'))['rating__avg']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'order', 'description']

class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'id', 'module', 'title', 'video_file', 'video_url',
            'duration', 'order', 'thumbnail', 'thumbnail_url',
            'description', 'created_at', 'transcript', 'is_preview'
        ]
        extra_kwargs = {
            'video_file': {'write_only': True},
            'thumbnail': {'write_only': True},
        }

    def get_video_url(self, obj):
        if obj.video_file:
            return self.context['request'].build_absolute_uri(obj.video_file.url)
        return None

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)
        return None

class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'course', 'subscribed_at', 'active']

class UserProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'video', 'timestamp', 'completed', 'last_play_time']

class CourseReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    rating_display = serializers.CharField(source='get_rating_display', read_only=True)

    class Meta:
        model = CourseReview
        fields = ['id', 'user', 'course', 'rating', 'rating_display', 'comment', 'created_at']