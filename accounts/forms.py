from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext as _

from .widgets import BootstrapFileInput, PasswordMeterInput
from .validation import UserValidationMixin


class CustomUserCreationForm(UserCreationForm, UserValidationMixin):
    email2 = forms.EmailField(label='Confirm Email')
    avatar = forms.ImageField(
        label='',
        widget=BootstrapFileInput(custom_label='Upload profile image'))

    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'email',
            'email2',
            'first_name',
            'last_name',
            'dob',
            'bio',
            'avatar',
            'favorite_animal',
            'hobbies',
            'password1',
            'password2',
        ]
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordMeterInput()
        self.fields['password1'].help_text = ''


class EditProfileForm(forms.ModelForm, UserValidationMixin):
    email2 = forms.EmailField(
        label='',
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Confirm Email'})
    )

    class Meta:
        fields = [
            'email',
            'email2',
            'first_name',
            'last_name',
            'dob',
            'bio',
            'favorite_animal',
            'hobbies'
        ]
        exclude = ('avatar',)
        model = get_user_model()


class MeterPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=PasswordMeterInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='',
    )