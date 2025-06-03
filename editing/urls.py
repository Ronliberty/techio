from django.urls import path

from .views import *


app_name = 'editing'
urlpatterns = [
    path('edit-hub/', EditingHubView.as_view(), name='editing-hub'),
    path('services/', EditingServiceListView.as_view(), name='editservice_list'),
    path('services/create/', EditingServiceCreateView.as_view(), name='editservice_create'),
    path('services/<int:pk>/', EditingServiceDetailView.as_view(), name='editservice_detail'),
    path('services/<int:pk>/update/', EditingServiceUpdateView.as_view(), name='editservice_update'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('editor/<int:pk>/', EditorProfileDetailView.as_view(), name='editorprofile_detail'),
    path('editor/<int:pk>/update/', EditorProfileUpdateView.as_view(), name='editorprofile_update'),
    path('services/<int:pk>/revision/', RevisionCreateView.as_view(), name='revision_create'),
    path('services/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]