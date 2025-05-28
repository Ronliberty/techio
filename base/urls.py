from django.urls import path
from .views import IndexView, CommunityView, InforView, ErrorView, HelpCenterView


app_name = 'base'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('community/', CommunityView.as_view(), name='community'),
    path('information/', InforView.as_view(), name='infor-index'),
    path('error/', ErrorView.as_view(), name='error-index'),
    path('help-center/', HelpCenterView.as_view(), name='help-center')



]