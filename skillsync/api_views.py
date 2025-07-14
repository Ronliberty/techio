from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    Category, InstructorProfile, AcademicService, OrderAssign,
    Course, Module, Video, Subscription, UserProgress, CourseReview
)
from .serializers import (
    CategorySerializer, InstructorProfileSerializer, AcademicServiceSerializer,
    OrderAssignSerializer, CourseSerializer, ModuleSerializer, VideoSerializer,
    SubscriptionSerializer, UserProgressSerializer, CourseReviewSerializer
)
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        if not request.user.is_staff:
            return Response(
                {'error': 'Only staff can approve instructors'},
                status=status.HTTP_403_FORBIDDEN
            )

        profile = self.get_object()
        profile.approved = True
        profile.save()
        return Response({'status': 'instructor approved'})


class AcademicServiceViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return AcademicService.objects.all()
        return AcademicService.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def assign_expert(self, request, pk=None):
        if not request.user.is_staff:
            return Response(
                {'error': 'Only staff can assign experts'},
                status=status.HTTP_403_FORBIDDEN
            )

        service = self.get_object()
        expert_id = request.data.get('expert_id')
        if not expert_id:
            return Response(
                {'error': 'expert_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        expert = get_object_or_404(InstructorProfile, id=expert_id)
        service.assigned_expert = expert
        service.status = 'ASSIGNED'
        service.save()

        return Response({'status': 'expert assigned'})


class OrderAssignViewSet(viewsets.ModelViewSet):
    serializer_class = OrderAssignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return OrderAssign.objects.all()
        return OrderAssign.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def modules(self, request, slug=None):
        course = self.get_object()
        modules = course.modules.all().order_by('order')
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Module.objects.filter(course_id=course_id).order_by('order')

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        serializer.save(course=course)


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        module_id = self.kwargs.get('module_id')
        return Video.objects.filter(module_id=module_id).order_by('order')

    def perform_create(self, serializer):
        module_id = self.kwargs.get('module_id')
        module = get_object_or_404(Module, id=module_id)
        serializer.save(module=module)


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        progress = self.get_object()
        progress.completed = True
        progress.save()
        return Response({'status': 'video marked as completed'})


class CourseReviewViewSet(viewsets.ModelViewSet):
    serializer_class = CourseReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return CourseReview.objects.filter(course_id=course_id)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        serializer.save(user=self.request.user, course=course)