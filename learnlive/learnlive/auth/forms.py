# Create your forms here
# This class was written by Abhinav Khanna
# This class is property of LearnLive Inc.
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserProfileForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    is_tutor = forms.BooleanField()
    profile_name = forms.CharField(max_length=50)

    def clean_email(self):
        new_email = self.cleaned_data.get('email')
        user_list = User.objects.filter(email=new_email)
        if len(user_list) > 0:
            raise ValidationError('This user already exists in our system.')
        return new_email
