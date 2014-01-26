# Create your forms here
# This class is property of LearnLive Inc.
# This class was written by Abhinav Khanna
from django import forms
from django.contrib.auth import authenticate
from learnlive.auth.forms import UserProfileForm
from learnlive.auth.views import CreateUserView

class CreateSessionForm(forms.Form):
    """
    This is a form that preprocesses all the information given
    in the creation of a session
    """
    id_user = forms.IntegerField()
    id_tutor = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField()
    confirm = forms.CharField()
    is_register = forms.BooleanField()

    def __init__(self, user, *args, **kwargs):
        super(CreateSessionForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        if user.is_authenticated:
            self.cleaned_data['id_user'] = user.id
            if self.cleaned_data.get('id_tutor') < 0:
                raise ValidationError("Invalid tutor id")
        else:
            # if they are not authenticated you either have a new orr an existing user
            if self.cleaned_data.get('is_register') == True:
                user_reg_form = UserProfileForm(self.cleaned_data)
                if user_reg_form.is_valid():
                    CreateUserView.create_user(user_reg_form)
                else
                    raise ValidationError("Registration error try again")
            else:
                # just a log in.
                user_log = authenticate(username=email, password=password)
                if user_log is None:
                    raise ValidationError('Incorrect login')
        return self.cleaned_data



