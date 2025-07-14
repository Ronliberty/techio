from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, UserProject, EditingService
from .serializers import (
    ProjectSerializer,
    UserProjectSerializer,
    EditingServiceSerializer
)
from django.shortcuts import get_object_or_404


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProjectViewSet(viewsets.ModelViewSet):
    serializer_class = UserProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProject.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        user_project = self.get_object()
        user_project.accepted = True
        user_project.status = 'ongoing'
        user_project.save()
        return Response({'status': 'project accepted'})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        user_project = self.get_object()
        user_project.status = 'completed'
        user_project.save()
        return Response({'status': 'project marked as completed'})


class EditingServiceViewSet(viewsets.ModelViewSet):
    serializer_class = EditingServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return EditingService.objects.all()
        return EditingService.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def assign_editor(self, request, pk=None):
        if not request.user.is_staff:
            return Response(
                {'error': 'Only staff can assign editors'},
                status=status.HTTP_403_FORBIDDEN
            )

        service = self.get_object()
        editor_id = request.data.get('editor_id')
        if not editor_id:
            return Response(
                {'error': 'editor_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # You would need to implement EditorProfile model and logic here
        # For now, we'll just assign any user as editor
        from django.contrib.auth import get_user_model
        User = get_user_model()
        editor = get_object_or_404(User, id=editor_id)

        service.assigned_editor = editor
        service.status = 'ASSIGNED'
        service.save()

        return Response({'status': 'editor assigned'})