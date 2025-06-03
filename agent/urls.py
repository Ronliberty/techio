from django.urls import path
from .views import *

urlpatterns = [
    # Agent URLs
    path('agents/', AgentListView.as_view(), name='agent_list'),
    path('agents/<slug:slug>/', AgentDetailView.as_view(), name='agent_detail'),
    path('agents/create/', AgentCreateView.as_view(), name='agent_create'),
    path('agents/<slug:slug>/update/', AgentUpdateView.as_view(), name='agent_update'),

    # Agent Image URLs
    path('agents/<slug:slug>/add-image/', AgentImageCreateView.as_view(), name='agentimage_create'),
    path('agent-images/<int:pk>/delete/', AgentImageDeleteView.as_view(), name='agentimage_delete'),

    # Ticket URLs
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('tickets/<slug:slug>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<slug:slug>/update/', TicketUpdateView.as_view(), name='ticket_update'),

    # Information URLs
    path('informations/', InformationListView.as_view(), name='information_list'),
    path('informations/<slug:slug>/', InformationDetailView.as_view(), name='information_detail'),
    path('informations/create/', InformationCreateView.as_view(), name='information_create'),
    path('informations/<slug:slug>/update/', InformationUpdateView.as_view(), name='information_update'),
    path('informations/<slug:slug>/delete/', InformationDeleteView.as_view(), name='information_delete'),

    # Information Media URLs
    path('informations/<slug:slug>/add-image/', InformationImageCreateView.as_view(),
         name='informationimage_create'),
    path('informations/<slug:slug>/add-video/', InformationVideoCreateView.as_view(),
         name='informationvideo_create'),
    path('media/<str:media_type>/<int:pk>/delete/', InformationMediaDeleteView.as_view(),
         name='informationmedia_delete'),
]