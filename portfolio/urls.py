# urls.py
from django.urls import path
from .views import  SkillCreateView, PortfolioHubView, ContactSubmissionListView,HeroContentUpdateView, HeroContentListView, HeroContentDetailView, HeroContentCreateView, HeroContentDeleteView, ContactSubmissionDetailView, ProjectDetailView, ProjectDeleteView,  SkillDeleteView, ContactInfoListView, ContactInfoCreateView, ContactInfoDeleteView, ProjectsListView, SkillsListView, ContactInfoView, FooterContentView, ProjectCreateView, SkillCategoryUpdateView, ContactInfoUpdateView, ProjectUpdateView,  SocialLinkListView, SocialLinkCreateView, SocialLinkUpdateView, SocialLinkDeleteView


app_name = 'portfolio'
urlpatterns = [
    path('portfolio-hub/', PortfolioHubView.as_view(), name='portfolio-hub'),

    path("hero/", HeroContentListView.as_view(), name="hero_list"),
    path("hero/create/", HeroContentCreateView.as_view(), name="hero_create"),
    path("hero/<slug:slug>/", HeroContentDetailView.as_view(), name="hero_detail"),
    path("hero/<slug:slug>/delete/", HeroContentDeleteView.as_view(), name="hero_delete"),
    path("hero/<slug:slug>/update/", HeroContentUpdateView.as_view(), name="hero_update"),

    path('skills/', SkillsListView.as_view(), name='skills_list'),
    path('admin/skills/edit/<slug:slug>/', SkillCategoryUpdateView.as_view(), name='skill_category_edit'),
    path('skills/create/', SkillCreateView.as_view(), name='skill_create'),
    path('skills/delete/<slug:slug>/', SkillDeleteView.as_view(), name='skill_delete'),


    path('contact/', ContactInfoView.as_view(), name='contact_info'),
    path('contact-info/', ContactInfoListView.as_view(), name='contact_info_list'),
    path('contact-info/create/', ContactInfoCreateView.as_view(), name='contact_info_create'),
    path('contact-info/<slug:slug>/update/', ContactInfoUpdateView.as_view(), name='contact_info_update'),
    path('contact-info/<slug:slug>/delete/', ContactInfoDeleteView.as_view(), name='contact_info_delete'),

    path("projects/", ProjectsListView.as_view(), name="project_list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
    path("projects/<slug:slug>/update/", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/<slug:slug>/delete/", ProjectDeleteView.as_view(), name="project_delete"),

    path("social-links/", SocialLinkListView.as_view(), name="social_list"),
    path("social-links/create/", SocialLinkCreateView.as_view(), name="social_create"),
    path("social-links/update/<int:pk>/", SocialLinkUpdateView.as_view(), name="social_update"),
    path("social-links/delete/<int:pk>/", SocialLinkDeleteView.as_view(), name="social_delete"),

    path('footer/', FooterContentView.as_view(), name='footer_content'),
    path('submissions/', ContactSubmissionListView.as_view(), name='contact-submission-list'),
    path('submissions/<slug:slug>/', ContactSubmissionDetailView.as_view(), name='contact-submission-detail'),




]