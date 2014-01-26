# Create your forms here
# This class was written by Abhinav Khanna
# This class is property of LearnLive Inc.
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserProfileForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        new_email = self.cleaned_data.get('email')
        user_list = User.objects.filter(email=new_email)
        if len(user_list) > 0:
            raise ValidationError('This user already exists in our system.')
        else:
            return new_email

    def clean(self):
        """
        This function will clean the registration form
        """
        # check that the passwords are the same
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password != confirm:
            raise ValidationError('The confirmation did not match the password')
        else:
            return self.cleaned_data
