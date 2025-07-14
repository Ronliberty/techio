from rest_framework import viewsets, permissions
from .models import (
    ProjectTag, Project, SkillCategory, Skill,
    ContactInfo, SocialLink, LegalLink, HeroContent,
    ContactSubmission, PortfolioSection, PortfolioTemplate,
    UserPortfolio, PortfolioContent, ContentTag
)
from .serializers import (
    ProjectTagSerializer, ProjectSerializer, SkillCategorySerializer,
    SkillSerializer, ContactInfoSerializer, SocialLinkSerializer,
    LegalLinkSerializer, HeroContentSerializer, ContactSubmissionSerializer,
    PortfolioSectionSerializer, PortfolioTemplateSerializer,
    UserPortfolioSerializer, PortfolioContentSerializer, ContentTagSerializer
)

class ProjectTagViewSet(viewsets.ModelViewSet):
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LegalLinkViewSet(viewsets.ModelViewSet):
    queryset = LegalLink.objects.all()
    serializer_class = LegalLinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HeroContentViewSet(viewsets.ModelViewSet):
    queryset = HeroContent.objects.all()
    serializer_class = HeroContentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PortfolioSectionViewSet(viewsets.ModelViewSet):
    queryset = PortfolioSection.objects.all()
    serializer_class = PortfolioSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PortfolioTemplateViewSet(viewsets.ModelViewSet):
    queryset = PortfolioTemplate.objects.all()
    serializer_class = PortfolioTemplateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserPortfolioViewSet(viewsets.ModelViewSet):
    queryset = UserPortfolio.objects.all()
    serializer_class = UserPortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PortfolioContentViewSet(viewsets.ModelViewSet):
    queryset = PortfolioContent.objects.all()
    serializer_class = PortfolioContentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContentTagViewSet(viewsets.ModelViewSet):
    queryset = ContentTag.objects.all()
    serializer_class = ContentTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]