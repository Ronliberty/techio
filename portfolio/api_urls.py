from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    ProjectTagViewSet, ProjectViewSet, SkillCategoryViewSet,
    SkillViewSet, ContactInfoViewSet, SocialLinkViewSet,
    LegalLinkViewSet, HeroContentViewSet, ContactSubmissionViewSet,
    PortfolioSectionViewSet, PortfolioTemplateViewSet,
    UserPortfolioViewSet, PortfolioContentViewSet, ContentTagViewSet
)

router = DefaultRouter()
router.register(r'project-tags', ProjectTagViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skill-categories', SkillCategoryViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact-info', ContactInfoViewSet)
router.register(r'social-links', SocialLinkViewSet)
router.register(r'legal-links', LegalLinkViewSet)
router.register(r'hero-content', HeroContentViewSet)
router.register(r'contact-submissions', ContactSubmissionViewSet)
router.register(r'portfolio-sections', PortfolioSectionViewSet)
router.register(r'portfolio-templates', PortfolioTemplateViewSet)
router.register(r'user-portfolios', UserPortfolioViewSet)
router.register(r'portfolio-content', PortfolioContentViewSet)
router.register(r'content-tags', ContentTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]