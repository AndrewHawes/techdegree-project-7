from django.db import models
from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class DatePickerField(models.DateField):
    class FormField(forms.DateField):
        widget = DatePickerInput(
            options={'keepInvalid': True, 'useCurrent': False}
        )
        input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']

    def formfield(self, **kwargs):
        defaults = {'form_class': DatePickerField.FormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
