from django import forms
from .models import *


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = '__all__'



class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class HeroContentForm(forms.ModelForm):
    class Meta:
        model = HeroContent
        fields = '__all__'