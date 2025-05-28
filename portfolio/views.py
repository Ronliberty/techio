# views.py
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.core import serializers
from .forms import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render ,redirect,  get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.loader import render_to_string


@method_decorator(cache_page(60 * 15), name='dispatch')


class ContactSubmissionListView(ListView):
    model = ContactSubmission
    template_name = 'portfolio/contact/subs.html'
    context_object_name = 'submissions'

    def get(self, request, *args, **kwargs):
        is_htmx = self.request.headers.get('HX-Request') == 'true'

        if not is_htmx:
            self.template_name = 'dashboard/manager_dashboard.html' # Redirect non-HTMX requests

        return super().get(request, *args, **kwargs)

class ContactSubmissionDetailView(DetailView):
    model = ContactSubmission
    template_name = 'portfolio/contact/detail.html'
    context_object_name = 'submission'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get(self, request, *args, **kwargs):
        is_htmx = self.request.headers.get('HX-Request') == 'true'

        if not is_htmx:
            self.template_name = 'dashboard/manager_dashboard.html' # Redirect non-HTMX requests

        return super().get(request, *args, **kwargs)

class HeroContentDetailView(DetailView):
    model = HeroContent
    template_name = "portfolio/hero/detail.html"
    context_object_name = "hero"

class HeroContentCreateView(CreateView):
    model = HeroContent
    form_class = HeroContentForm
    template_name = "portfolio/hero/form.html"
    success_url = reverse_lazy("base:hero_list")

    def form_valid(self, form):
        form.save()
        return JsonResponse({"message": "Hero content created successfully"}, status=201)

class HeroContentDeleteView(DeleteView):
    model = HeroContent
    template_name = "portfolio/hero/delete.html"
    success_url = reverse_lazy("base:hero_list")

    def delete(self, request, *args, **kwargs):
        hero = self.get_object()
        hero.delete()
        return HttpResponse(status=204)

class HeroContentListView(ListView):
    model = HeroContent
    template_name = "portfolio/hero/list.html"
    context_object_name = "heroes"

class HeroContentUpdateView(UpdateView):
    model = HeroContent
    form_class = HeroContentForm
    template_name = "base/hero/form.html"

    def get_success_url(self):
        return reverse_lazy("base:hero_list")

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({"message": "Hero content updated successfully"}, status=200)

class ProjectsListView(ListView):
    model = Project
    template_name = "portfolio/projects/list.html"
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = "base/projects/detail.html"
    context_object_name = "project"

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "portfolio/projects/form.html"
    success_url = reverse_lazy("base:project_list")

    def form_valid(self, form):
        project = form.save()
        return JsonResponse({"message": "Project created successfully", "id": project.id}, status=201)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "portfolio/projects/delete.html"
    success_url = reverse_lazy("base:project_list")

    def delete(self, request, *args, **kwargs):
        project = self.get_object()
        project.delete()
        return HttpResponse(status=204)

class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'base/projects/form.html'
    success_url = reverse_lazy("base:project_list")



class SkillsListView(ListView):
    model = SkillCategory
    template_name = "portfolio/skill/list.html"
    context_object_name = 'skill_categories'

    def get_queryset(self):
        return SkillCategory.objects.prefetch_related('skills')

class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'portfolio/skill/form.html'
    success_url = reverse_lazy('skills_list')

class SkillCategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = SkillCategory
    form_class = SkillCategoryForm
    template_name = 'portfolio/partials/category_form.html'
    success_message = "Skill category updated successfully"

    def get_success_url(self):
        return reverse_lazy('base:skills_list')

class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'portfolio/skills/delete.html'
    success_url = reverse_lazy('base:skills_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def delete(self, request, *args, **kwargs):
        skill = get_object_or_404(Skill, slug=self.kwargs['slug'])
        skill.delete()

        if request.headers.get('HX-Request'):  # If the request is from HTMX
            skills = Skill.objects.all()
            html = render_to_string('skills/skills_list.html', {'skills': skills}, request=request)
            return HttpResponse(html)

        return super().delete(request, *args, **kwargs)

class ContactInfoView(TemplateView):
    template_name = "portfolio/partials/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        return context


class ContactInfoListView(ListView):
    model = ContactInfo
    template_name = "portfolio/contact/list.html"
    context_object_name = "contacts"


class ContactInfoCreateView(CreateView):
    model = ContactInfo
    template_name = "base/contact/form.html"
    fields = ["email", "phone", "address", "is_active"]
    success_url = reverse_lazy("base:contact_info_list")

    def form_valid(self, form):
        # Ensure only one active contact info exists
        if form.cleaned_data.get("is_active"):
            ContactInfo.objects.filter(is_active=True).update(is_active=False)

        # Generate slug
        instance = form.save(commit=False)
        if not instance.slug:
            base_slug = slugify("contact-info")
            instance.slug = base_slug
            for i in itertools.count(1):
                if not ContactInfo.objects.filter(slug=instance.slug).exists():
                    break
                instance.slug = f"{base_slug}-{i}"
        instance.save()
        return super().form_valid(form)


class ContactInfoUpdateView(UpdateView):
    model = ContactInfo
    template_name = "base/contact/form.html"
    fields = ["email", "phone", "address", "is_active"]
    success_url = reverse_lazy("base:contact_info_list")


class ContactInfoDeleteView(DeleteView):
    model = ContactInfo
    template_name = "portfolio/contact/delete.html"
    success_url = reverse_lazy("base:contact_info_list")

class FooterContentView(TemplateView):
    template_name = "portfolio/partials/footer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'social_links': SocialLink.objects.all(),
            'legal_links': LegalLink.objects.all()
        })
        return context








class SocialLinkListView(ListView):
    model = SocialLink
    template_name = "portfolio/socials/list.html"
    context_object_name = "social_links"

class SocialLinkCreateView(CreateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = "portfolio/socials/form.html"
    success_url = reverse_lazy("base:social_list")

class SocialLinkUpdateView(UpdateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = "portfolio/socials/form.html"
    success_url = reverse_lazy("base:social_list")

class SocialLinkDeleteView(DeleteView):
    model = SocialLink
    template_name = "portfolio/socials/delete.html"
    success_url = reverse_lazy("base:social_list")