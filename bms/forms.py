from django import forms
from .models import Post, News, Tool, Skill, Service, ServiceResponse, ServiceRequest


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['']


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['']

class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = ServiceResponse
        fields = ['']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['']