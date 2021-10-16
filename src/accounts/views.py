from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from accounts.forms import UserRegistrationForm


class UserRegistrationView(generic.CreateView):
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
