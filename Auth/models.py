from django.db import models
from django.contrib.auth.models import User 
from Company.department import DEPARTMENT, STATES

class UserDetail(models.Model):

    user  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    course = models.CharField(max_length=100, choices=DEPARTMENT, null=True, blank=True)
    state = models.CharField(choices=STATES, max_length=15)
    is_attending_tutorial = models.BooleanField(default=False)
    utme_attempts = models.IntegerField(default=1)
    whatsapp = models.URLField(null=True, blank=True)
    know_about_us = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
