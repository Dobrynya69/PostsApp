from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import LoginForm, SignupForm

class CustomUserCreationForm(SignupForm):
    image = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].label = ''
    

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        if request.FILES:
            user.image = request.FILES['image']
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.save()
        return user


class CustomUserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].label = ''
        field = self.fields['remember']
        field.widget = field.hidden_widget()


class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    image = forms.ImageField(required=False)


    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].label = ''


    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'image']