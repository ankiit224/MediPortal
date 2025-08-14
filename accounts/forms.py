from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, widget=forms.RadioSelect)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    pincode = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'first_name','last_name','username','email','user_type',
            'profile_picture','address_line1','city','state','pincode',
            'password1','password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email is already in use.')
        return email
