from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    NewsListView,
    NewsDetailView,
    NewsCreateView,
    NewsDeleteView,
    ToolsListView,
    ToolsDetailView,
    ToolsCreateView,
    ToolsDeleteView,
    SkillsView,
    SkillsDetailView,
    SkillsCreateView,
    SkillsDeleteView,
    ServiceListView,
    CreateServiceView,
    DeleteServiceView,
    DetailServiceView,
    CreateRequestServiceView,
    RequestView,
    DetailUserRequestView,
    DeleteUserRequestView,
    DetailRequestView,
    RequestListsView,
    CreateResponseView,
    DetailResponseView,
    ListResponseView,
    DeleteResponseView,
    UserResponseView,
    UserDetailedResponseView

)

app_name = 'bms'

urlpatterns = [
    #post
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('create/post/', PostCreateView.as_view(), name='post-create'),
    path('delete/post/<slug:slug>/', PostDeleteView.as_view(), name='delete-post'),




    #news
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
    path('create/news/', NewsCreateView.as_view(), name='news-create'),
    path('delete/news/<slug:slug>/', NewsDeleteView.as_view(), name='delete-news'),


    #tools
    path('tools/', ToolsListView.as_view(), name='tools-list'),
    path('tools/<slug:slug>/', ToolsDetailView.as_view(), name='tools-detail'),
    path('create/tools/', ToolsCreateView.as_view(), name='tools-create'),
    path('delete/tools/<slug:slug>/', ToolsDeleteView.as_view(), name='delete-tools'),



    #skills
    path('skills/', SkillsView.as_view(), name='skills-list'),
    path('skills/<slug:slug>/', SkillsDetailView.as_view(), name='skills-detail'),
    path('create/skills/', SkillsCreateView.as_view(), name='skills-create'),
    path('delete/skills/<slug:slug>/', SkillsDeleteView.as_view(), name='delete-skills'),



    #SERVICE
    path('service/', ServiceListView.as_view(), name='service-list'),
    path('create/service/', CreateServiceView.as_view(), name='service-create'),

    path('delete/service/<slug:slug>/', DeleteServiceView.as_view(), name='delete-service'),
    path('detail/service/<slug:slug>/', DetailServiceView.as_view(), name='detail-service'),




    #requets

    path('create/request/', CreateRequestServiceView.as_view(), name='request-create'),
    path('request', RequestView.as_view(), name='request-list'),
    path('user/request/<slug:slug>/', DetailUserRequestView.as_view(), name='user-request'),
    path('delete/request/<slug:slug>/', DeleteUserRequestView.as_view(), name='delete-request'),

    #manager
    path('detail/request/<slug:slug>/', DetailRequestView.as_view(), name='detail-request'),
    path('list/requests/', RequestListsView.as_view(), name='list-manager'),


    #response
    #manager
    path('create/response/<slug:slug>/', CreateResponseView.as_view(), name='response-create'),
    path('response/detail/<slug:slug>/', DetailResponseView.as_view(), name='detail-response'),
    path('list/response/', ListResponseView.as_view(), name='list-response'),
    path('delete/response/<slug:slug>/', DeleteResponseView.as_view(), name='delete-response'),

    #default
    path('user/response/', UserResponseView.as_view(), name='user-response'),
    path('detailed/response/<slug:slug>/', UserDetailedResponseView.as_view(), name='detailed-response'),

    ]