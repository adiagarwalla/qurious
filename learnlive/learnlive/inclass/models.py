from django.db import models
from learnlive.auth.models import UserProfile

# Create your models here.
class Session(models.Model):
    """
    This is a session object, it contains information regarding a new
    in class session. This information is what allows someone to gain
    access to the url that grants entry into the session.
    """
    id_tutor = models.ForeignKey(UserProfile)
    id_user = models.ForeignKey(UserProfile, related_name='id_tutee')
    time = models.IntegerField()
    session_key = models.TextField()

class InClassNotification(models.Model):
    """
    This is the notification object that is used to create and generate
    an in class notification.
    """
    id_from = models.ForeignKey(UserProfile)
    message = models.TextField()
    m_type = models.IntegerField() # This will have to be carefully done
    url_inclass = models.CharField(max_length=512)

