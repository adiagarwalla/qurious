from django.db import models

# Create your models here.

class Skill(models.Model):

    name = models.CharField(max_length=512)
    lemma_name = models.CharField(max_length=512)
    is_marketable = models.BooleanField()
    num_endorsements = models.IntegerField()
    price = models.IntegerField()
