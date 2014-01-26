# Create your forms here
# This class is property of LearnLive Inc.
# This class was written by Abhinav Khanna
from django import forms

class CreateSessionForm(forms.Form):
    """
    This is a form that preprocesses all the information given
    in the creation of a session
    """
    def __init__(self, user, *args, **kwargs):
        super(CreateSessionForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        if user.is_authenticated:
            self.cleaned_data['id_user'] = user.id
            if self.cleaned_data.get('id_tutor') < 0:
                raise ValidationError("Invalid tutor id")


