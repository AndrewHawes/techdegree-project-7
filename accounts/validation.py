import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class UserValidationMixin:
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email and email2 and email != email2:
            raise ValidationError(
                _("Email addresses don't match!"),
                code='email_no_match'
            )
        return email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_bio(self):
        """
        Make sure bio is at least 10 characters.
        Parse HTML and strip tags to get real character count.
        """
        bio = self.cleaned_data.get('bio')
        tag_pattern = r'<.*?>'
        charref_pattern = r'&[\w\d]+;'
        stripped = re.sub(tag_pattern, '', bio)
        stripped = re.sub(charref_pattern, ' ', stripped)
        if len(stripped) < 10:
            raise ValidationError(
                _("Bio must be at least 10 characters."),
                code='bio_too_short'
            )
        return bio