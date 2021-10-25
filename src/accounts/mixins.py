from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class LoginAndStaffRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is staff."""

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_authenticated and request.user.is_staff):
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
