from django.db import models
from Company.department import DEPARTMENT


class Data(models.Model):
    utme = models.IntegerField()
    putme = models.IntegerField()
    department = models.CharField(choices=DEPARTMENT, max_length=50)
    year_of_admission = models.IntegerField()
    number_of_attempts = models.IntegerField()
    
    def __str__(self):
        return f'{self.department} - {self.utme}'
    
class AspirantData(models.Model):
    
    department = models.CharField(max_length=40)
    year = models.CharField( max_length=10)