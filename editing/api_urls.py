from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'projects', api_views.ProjectViewSet, basename='project')
router.register(r'user-projects', api_views.UserProjectViewSet, basename='userproject')
router.register(r'editing-services', api_views.EditingServiceViewSet, basename='editingservice')

urlpatterns = [
    path('', include(router.urls)),
]