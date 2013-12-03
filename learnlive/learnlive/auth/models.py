from django.db import models
from django.contrib.auth.models import User 
from learnlive.bid_platform.models import Skill 

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User)
    profile_name = models.CharField(max_length=256)
    skills = models.ForeignKey(Skill, null=True)

