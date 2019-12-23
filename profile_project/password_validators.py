import re

from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
from django.core.exceptions import ValidationError, FieldDoesNotExist
from django.utils.translation import ugettext as _


class RegexValidator:
    message = ''
    pattern = ''
    code = ''

    def validate(self, password, user=None):
        if not re.findall(self.pattern, password):
            raise ValidationError(
                _(self.message),
                code=self.code
            )

    def get_help_text(self):
        return _(self.message)


class NumberValidator(RegexValidator):
    message = 'Your password must contain at least one number.'
    pattern = r'\d'
    code = 'password_no_number'


class UppercaseValidator(RegexValidator):
    message = 'Your password must contain at least one uppercase letter.'
    pattern = '[A-Z]'
    code = 'password_no_uppercase'


class LowercaseValidator(RegexValidator):
    message = 'Your password must contain at least one lowercase letter.'
    pattern = '[a-z]'
    code = 'password_no_lowercase'


class SpecialCharacterValidator(RegexValidator):
    message = 'Your password must contain at least one special character.'
    pattern = r'[\[\]()\{}|`~!@#$%^&/*_\-+=;:\'\",<>.\/\\?]'
    code = 'password_no_special_character'


class NameNotInPasswordValidator:
    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in ['username', 'first_name', 'last_name']:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            if value.lower() in password.lower():
                try:
                    verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                except FieldDoesNotExist:
                    verbose_name = attribute_name
                raise ValidationError(
                    _("The password contains your %(verbose_name)s."),
                    code='password_contains_name',
                    params={'verbose_name': verbose_name},
                )

    def get_help_text(self):
        return _('Your password can’t contain your username or any part of your full name.')


