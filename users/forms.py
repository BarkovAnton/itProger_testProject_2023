from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

class RegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        
    def _post_clean(self, *args, **kwargs):
        super(RegForm, self)._post_clean(*args, **kwargs)

        password = self.cleaned_data.get('password1')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password1', error)


class UserUpdate(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']

