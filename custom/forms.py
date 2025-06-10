from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
CustomUser = get_user_model()

class CustomUserSignupForm(SignupForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    country = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'})
    )

    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "country", "password1", "password2")

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.country = self.cleaned_data['country']
        user.save()
        return user
class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
class CustomUserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'country', 'is_active', 'password']




class DeleteAccountForm(forms.Form):
    password = forms.CharField(
        label=_("Current Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        required=True
    )

    confirm = forms.BooleanField(
        label=_("I understand this action is irreversible"),
        required=True,
        widget=forms.CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm')

        if not confirm:
            raise ValidationError(_("You must confirm account deletion"))

        if self.user.has_usable_password():
            if not authenticate(username=self.user.username, password=password):
                raise ValidationError(_("The password you entered is incorrect"))

        return cleaned_data