from django.urls import path

from . views import *

app_name = 'todo'
urlpatterns = [
    # TaskList URLs
    path('tasklists/', TaskListListView.as_view(), name='tasklist-list'),
    path('tasklists/create/', TaskListCreateView.as_view(), name='tasklist-create'),
    path('tasklists/<int:pk>/', TaskListDetailView.as_view(), name='tasklist-detail'),
    path('tasklists/<int:pk>/update/', TaskListUpdateView.as_view(), name='tasklist-update'),
    path('tasklists/<int:pk>/delete/', TaskListDeleteView.as_view(), name='tasklist-delete'),

    # Task URLs
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    # Comment URLs
    path('tasks/<int:task_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Reminder URLs
    path('tasks/<int:task_id>/reminders/create/', ReminderCreateView.as_view(), name='reminder-create'),
    path('reminders/<int:pk>/delete/', ReminderDeleteView.as_view(), name='reminder-delete'),

    # Tag URLs
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]