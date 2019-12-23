import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from .forms import EditProfileForm, CustomUserCreationForm, MeterPasswordChangeForm

logger = logging.getLogger(__name__)


class SignUpView(CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        new_user = form.save()
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user is not None:
            login(self.request, user)
            messages.success(
                self.request,
                "You're now a user! You've been signed in, too."
            )
            return redirect(self.success_url)
        else:
            messages.error(
                self.request,
                'We encountered some difficulties trying to log you in. An '
                'administrator has been notified. Please try again later.'
            )
            logger.error(f'Couldn’t authenticate user: {new_user}, id: {new_user.id}')
            return redirect(reverse('home'))


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'


class EditProfileView(UpdateView, LoginRequiredMixin):
    template_name = 'accounts/edit.html'
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Profile updated successfully!')
        return reverse('profile')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = MeterPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password successfully changed.")
            return redirect(reverse('profile'))
    else:
        form = MeterPasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
