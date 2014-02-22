# Author Abhinav Khanna
from django import forms

class AddSkillForm(forms.Form):
    """
    This is the form for the basic add skill system
    """
    new_skill = forms.CharField()

    def clean(self):
       skill = self.cleaned_data.get('new_skill')
       skill = skill.lower()
       self.cleaned_data['new_skill'] = skill
       return self.cleaned_data


class EditSkillForm(forms.Form):
    """
    Form for cleaning edit / put input for Skills
    """
    skill_id = forms.IntegerField()
    price = forms.IntegerField()
    is_marketable = forms.IntegerField()
    desc = forms.CharField()

class EditProfileForm(forms.Form):
    """
    This is the form for processing the profile information
    """
    profile_name = forms.CharField()
    phone_number = forms.CharField(required=False)
    bio = forms.CharField(required=False)

class NotificationUpdateForm(forms.Form):
    """
    This is the form that handles the notification updates
    """
    notification_url = forms.CharField()
