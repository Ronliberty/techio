from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from . import api_views

# Main router
router = DefaultRouter()
router.register(r'categories', api_views.CategoryViewSet, basename='category')
router.register(r'instructors', api_views.InstructorProfileViewSet, basename='instructor')
router.register(r'academic-services', api_views.AcademicServiceViewSet, basename='academicservice')
router.register(r'orders', api_views.OrderAssignViewSet, basename='order')
router.register(r'courses', api_views.CourseViewSet, basename='course')

# Nested routers for course structure
courses_router = NestedSimpleRouter(router, r'courses', lookup='course')
courses_router.register(r'modules', api_views.ModuleViewSet, basename='module')
courses_router.register(r'reviews', api_views.CourseReviewViewSet, basename='review')

modules_router = NestedSimpleRouter(courses_router, r'modules', lookup='module')
modules_router.register(r'videos', api_views.VideoViewSet, basename='video')

# Other routers
router.register(r'subscriptions', api_views.SubscriptionViewSet, basename='subscription')
router.register(r'progress', api_views.UserProgressViewSet, basename='progress')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(courses_router.urls)),
    path('', include(modules_router.urls)),
]