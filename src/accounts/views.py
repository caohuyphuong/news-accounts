from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from .mixins import LoginAndStaffRequiredMixin
from accounts.forms import UserRegistrationForm, UserUpdateForm

User = get_user_model()


class UserRegistrationView(generic.CreateView):  # Create
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.set_password(get_random_string(length=8))
        user.save()
        send_mail(
            subject="Thank you for registration",
            message="We've received your registration. We will test and reply you soon.",
            from_email="admin@email.com",
            recipient_list=[user.email, ]
        )
        return super().form_valid(form)


class UserListView(LoginAndStaffRequiredMixin, generic.ListView):  # Read
    template_name = 'accounts/user_list.html'
    queryset = User.objects.all()  # User.objects.filter(is_active=False)


class UserDetailView(LoginAndStaffRequiredMixin, generic.DetailView):  # Read
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()


class UserUpdateView(LoginAndStaffRequiredMixin, generic.UpdateView):
    template_name = 'accounts/user_update.html'
    form_class = UserUpdateForm
    queryset = User.objects.all()
    success_url = reverse_lazy('accounts:user_list')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject="Your account was activated",
            message="You can reset password to login.",
            from_email="admin@email.com",
            recipient_list=[user.email, ]
        )
        return super().form_valid(form)
