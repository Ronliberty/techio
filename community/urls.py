from django.urls import path
from .views import (
    CreateGroupView,
    GroupListView,
    GroupEditView,
    GroupDeleteView,
    GroupLeaveView,
)


app_name = 'community'

urlpatterns = [
    path('create/group/', CreateGroupView.as_view(), name='create-group'),
    path('list/group/', GroupListView.as_view(), name='list-group'),
    path('edit/group/', GroupEditView.as_view(), name='edit-group'),
    path('delete/group/', GroupDeleteView.as_view(), name='delete-group'),
    path('leave/group/', GroupLeaveView.as_view(), name='leave-group'),
]