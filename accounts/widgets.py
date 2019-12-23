from django.forms import FileInput, PasswordInput


class BootstrapFileInput(FileInput):
    template_name = 'accounts/widgets/bootstrap_file_input.html'

    def __init__(self, custom_label=None, attrs=None):
        self.custom_label = custom_label
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        if attrs is None:
            attrs = {}
        if 'class' in attrs.keys():
            attrs['class'] += ' custom-file-input'
        else:
            attrs['class'] = 'custom-file-input'
        context = super().get_context(name, value, attrs)
        context['widget']['custom_label'] = self.custom_label
        return context


class PasswordMeterInput(PasswordInput):
    template_name = 'accounts/widgets/password_strength_meter.html'



