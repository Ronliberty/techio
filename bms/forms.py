from django import forms
from .models import Post, News, Tool, Skill, Service, ServiceResponse, ServiceRequest


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

class ResponseForm(forms.ModelForm):
    class Meta:
        model = ServiceResponse
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'