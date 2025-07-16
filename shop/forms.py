from django import forms
from .models import Category, Prod
from django.utils.text import slugify


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'display_order', 'parent_id', 'image', 'domain_user_id']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Customize domain_user_id field based on user group
        if self.user:
            if self.user.groups.filter(name='merchant').exists():
                # Merchants can only assign to themselves
                self.fields['domain_user_id'].initial = self.user
                self.fields['domain_user_id'].widget = forms.HiddenInput()

            elif self.user.groups.filter(name='default').exists():
                # Default users can't set domain user
                del self.fields['domain_user_id']

            # Managers see the full field as defined

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Auto-generated fields
        instance.slug = slugify(instance.name)
        instance.added_by_user_id = self.user

        if commit:
            instance.save()
        return instance

class ProdForm(forms.ModelForm):
    class Meta:
        model = Prod
        fields = [ 'category', 'name', 'description', 'specifications', 'image', 'initial_buying_price', 'initial_selling_price', 'weight', 'dimensions', 'uom', 'color', 'tax_percentage', 'brand', 'brand_model', 'seo_title' ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Customize domain_user_id field based on user group
        if self.user:
            if self.user.groups.filter(name='merchant').exists():
                # Merchants can only assign to themselves
                self.fields['domain_user_id'].initial = self.user
                self.fields['domain_user_id'].widget = forms.HiddenInput()

            elif self.user.groups.filter(name='default').exists():
                # Default users can't set domain user
                del self.fields['domain_user_id']

            # Managers see the full field as defined

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Auto-generated fields
        instance.slug = slugify(instance.name)
        instance.added_by_user_id = self.user

        if commit:
            instance.save()
        return instance