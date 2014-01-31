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
