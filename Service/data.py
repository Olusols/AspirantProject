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
    
class PredictChanceData(models.Model):
    '''
    This database table will be used to collect data from aspirant that 
    use the predict chance algorithm
    
    E.g
    department ==> Medicine and Surgery
    utme_score ==> 303
    chance ==> 71
    status ==> Worse, Bad, Good, Very Good, Excellent
    
    The status actually depend on the chance
       51 - 55 --> Worse
       55 - 68 --> Bad
       69 - 75 --> Good
       76 - 82 --> Very Good
       82 - 91 --> Excellent
    
    '''
    department = models.CharField(max_length=50)
    utme_score = models.IntegerField()
    chance = models.FloatField()
    status = models.CharField(max_length=10)
    
    def return_status(self):
        
        if self.chance >= 51 and self.chance < 55:
            return 'Worse'
        elif self.chance >= 55 and self.chance < 68:
            return 'Bad'
        elif self.chance >= 68 and self.chance < 75:
            return 'Good'
        elif self.chance >= 75 and self.chance < 82:
            return 'Very Good'
        else:
            return 'Excellent'
        
       
        
    
    
    def save(self, *args, **kwargs):
        if not self.status:
            self.status = PredictChanceData.return_status(self)
        super(PredictChanceData, self).save(*args, **kwargs)