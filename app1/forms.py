from django import forms
from django.contrib.auth.forms import SetPasswordForm as DjangoSetPasswordForm
# from .models import CustomUser

class CustomSetPasswordForm(DjangoSetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm New Password"

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                
            })
