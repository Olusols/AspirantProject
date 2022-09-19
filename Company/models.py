from django.db import models
from Company.department import STATES

class State(models.Model):
    state = models.CharField(choices=STATES, max_length=30)
    
    def __str__(self):
        return self.state


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.author:
            self.author = 'Anonymous'

        super(Quote, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.author
