from django.db import models
from treebeard.mp_tree import MP_Node

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

class Entity(MP_Node):
    """
    This is the entity class. It holds the name of the entity, the wiki
    page attached to the entity, and the children that spring from this entity
    """

    name = models.CharField(max_length=512)
    wiki_page = models.URLField(max_length=512)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Entity: %s' % self.name
