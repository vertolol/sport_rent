from django import forms
from cities_light.models import Region, City
from django.contrib.auth import get_user_model

from allauth.account.forms import LoginForm
''', SignupForm'''


class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget.attrs.update({'class': 'form-control'})
        self.fields["password"].widget.attrs.update({'class': 'form-control'})

    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    city = forms.ModelChoiceField(label="city",
                             queryset=City.objects.all(),
                             required=True)
    region = forms.ChoiceField(label="region",
                               choices=sorted(
                                    [(i.id, i.alternate_names.split(';')[-1]) for i in Region.objects.all()],
                                    key=lambda x: x[1]),
                               required=True)

    class Meta():
        model = get_user_model()
        fields = (
            'first_name', 'email', 'region', 'city'
        )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.city = self.cleaned_data['city']
        user.save()
        return user
