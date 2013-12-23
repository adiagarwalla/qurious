from django.db import models

# Create your models here.

class Skill(models.Model):

    name = models.CharField(max_length=512)
    #is_marketable = models.BooleanField()
