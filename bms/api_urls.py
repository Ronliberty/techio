# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'posts', api_views.PostViewSet, basename='post')
router.register(r'news', api_views.NewsViewSet, basename='news')
router.register(r'tools', api_views.ToolViewSet, basename='tool')
router.register(r'skills', api_views.SkillViewSet, basename='skill')
router.register(r'services', api_views.ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]