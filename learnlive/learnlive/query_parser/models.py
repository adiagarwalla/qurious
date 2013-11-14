from django.db import models

# Create your models here.
class Category(models.Model):
    """
    This is the category model. Tells what verbs are in what category
    """

    name = models.CharField(max_length=256)

class Verb(models.Model):
    """
    This is the verb class that holds the analyzed verb object
    """

    name = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category)
