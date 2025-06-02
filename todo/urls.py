from django.urls import path

from . views import *

app_name = 'todo'
urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task-list'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('delete-task/', DeleteTaskView.as_view(), name='task-delete'),
    path('comment-create/', CommentCreateView.as_view(), name='create-comment'),
    path('reminder/', TaskReminderView.as_view(), name='task-reminder'),

]