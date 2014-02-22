# Create your forms here
# This class is property of LearnLive Inc.
# This class was written by Abhinav Khanna
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login
from learnlive.auth.forms import UserProfileForm
from learnlive.auth.views import CreateUserView
from django.core.exceptions import ValidationError

class CreateSessionForm(forms.Form):
    """
    This is a form that preprocesses all the information given
    in the creation of a session
    """
    id_user = forms.CharField(required=False) # hack to allow the clean to be called
    id_tutor = forms.IntegerField()
    skill_price = forms.IntegerField()
    minutes = forms.IntegerField()
    email = forms.EmailField(required=False)
    password = forms.CharField(required=False)
    confirm = forms.CharField(required=False)
    options = forms.BooleanField(required=False)

    def __init__(self, request, *args, **kwargs):
        self.request = request 
        super(CreateSessionForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request.user.is_authenticated():
            self.cleaned_data['id_user'] = self.request.user.username
            if self.cleaned_data.get('id_tutor') < 0:
                raise ValidationError("Invalid tutor id")
        else:
            # if they are not authenticated you either have a new orr an existing user
            if self.cleaned_data.get('is_register') == True:
                user_reg_form = UserProfileForm(self.cleaned_data)
                if user_reg_form.is_valid():
                    CreateUserView.create_user(user_reg_form)
                else:
                    raise ValidationError("Registration error try again")
            else:
                # just a log in.
                import pdb; pdb.set_trace()
                user_log = authenticate(username=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
                if user_log is None:
                    raise ValidationError('Incorrect login')
                self.cleaned_data['id_user'] = user_log.username
                login(self.request, user_log)
        return self.cleaned_data

class MessageForm(forms.Form):
    """
    This is the message form, cleans the content and message information
    """
    content = forms.CharField()
    session_id = forms.CharField()

class ReviewForm(forms.Form):
    """
    This is a review form
    """
    rev_desc = forms.CharField(required=False)
    rev_stars = forms.IntegerField()
    tutor = forms.CharField()
