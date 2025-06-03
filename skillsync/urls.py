from django.urls import path

from .views import *


app_name = 'skillsync'

urlpatterns = [
    path('skill-hub/', SkillSyncHubView.as_view(), name='skill-hub'),
    path('category-create/', CreateCategoryView.as_view(), name='create-category'),
    path('list-category', ListCategoryView.as_view(), name='list-category'),
    path('delete-category', DeleteCategoryView.as_view(), name='delete-category'),
    path('inst-create', CreateInstructorView.as_view(), name='create-inst'),
    path('inst-list/', InstructorListView.as_view(), name='list-instructor'),
    path('inst-delete/', InstructorDeleteView.as_view(), name='delete-instructor'),

    path('services/', AcademicServiceListView.as_view(), name='academicservice_list'),
    path('services/create/', AcademicServiceCreateView.as_view(), name='academicservice_create'),
    path('services/<int:pk>/', AcademicServiceDetailView.as_view(), name='academicservice_detail'),
    path('services/<int:pk>/update/', AcademicServiceUpdateView.as_view(), name='academicservice_update'),

    path('orders/', OrderListView.as_view(), name='order_list'),

    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<slug:slug>/update/', CourseUpdateView.as_view(), name='course_update'),


    path('courses/<slug:slug>/modules/create/',ModuleCreateView.as_view(), name='module_create'),


    path('modules/<int:module_id>/videos/create/', VideoCreateView.as_view(), name='video_create'),




]