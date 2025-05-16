from django.contrib.auth.mixins import UserPassesTestMixin


class GroupRequiredMixin(UserPassesTestMixin):
    allowed_groups = ['manager', 'merchant', 'default']

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.allowed_groups).exists()