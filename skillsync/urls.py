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


]