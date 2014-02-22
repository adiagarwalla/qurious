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
    prof_from_username = models.CharField(max_length=512);
    message = models.TextField()
    m_type = models.IntegerField() # This will have to be carefully done
    url_inclass = models.CharField(max_length=512)
    seen = models.BooleanField()

class Message(models.Model):
    """
    This is a messages model
    """
    user_from = models.ForeignKey(UserProfile)
    user_from_name = models.CharField(max_length=512)
    seq_number = models.IntegerField()
    content = models.TextField()
    session = models.ForeignKey(Session)

class RSA(models.Model):
    """
    BAD SECURITY PRACTICE: Stores the RSAKey in the database for further use
    """
    public = models.TextField()
    private = models.TextField()
