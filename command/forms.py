from django import forms


class FunctionAdminForm(forms.ModelForm):
    def clean(self):
        if not self.cleaned_data['remote'] and self.cleaned_data['device'] is not None:
            raise forms.ValidationError('Error: A local (non remote) function must not have a device assigned.')
        if self.cleaned_data['remote'] and self.cleaned_data['device'] is None:
            raise forms.ValidationError('Error: A remote function must have a device assigned to it.')
