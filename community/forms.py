from django import forms
from .models import ChatGroup

from django.contrib.auth import get_user_model

user = get_user_model()


class GroupForm(forms.ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['']