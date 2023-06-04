from django import forms
from allauth.account.forms import LoginForm, SignupForm

class CustomUserCreationForm(SignupForm):
    image = forms.ImageField(required=False)

class CustomUserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        field = self.fields['remember']
        field.widget = field.hidden_widget()