from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    temp_code = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.user.email
