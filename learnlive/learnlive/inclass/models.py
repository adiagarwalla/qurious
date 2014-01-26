from django.db import models
from learnlive.auth.models import UserProfile

# Create your models here.
class Session(models.Model):
    """
    This is a session object, it contains information regarding a new
    in class session. This information is what allows someone to gain
    access to the url that grants entry into the session.
    """
    prof_tutor = models.ForeignKey(UserProfile)
    prof_user = models.ForeignKey(UserProfile, related_name='prof_tutee')
    time = models.IntegerField()
    session_key = models.TextField()
    is_cancelled = models.BooleanField()

class InClassNotification(models.Model):
    """
    This is the notification object that is used to create and generate
    an in class notification.
    """
    prof_from = models.ForeignKey(UserProfile)
    prof_to = models.ForeignKey(UserProfile, related_name="id_to")
    message = models.TextField()
    m_type = models.IntegerField() # This will have to be carefully done
    url_inclass = models.CharField(max_length=512)

def RSA(models.Model):
    """
    BAD SECURITY PRACTICE: Stores the RSAKey in the database for further use
    """
    public = models.TextField()
    private = models.TextField()
