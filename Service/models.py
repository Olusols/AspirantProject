from django.db import models
import numpy as np
from Company.department import DEPARTMENT, SUBJECT
from .prediction import linear, calculate_competitiveness

class Faculty(models.Model):
    faculty = models.CharField(max_length=30)

    def __str__(self):
        return self.faculty

class Department(models.Model):
    department = models.CharField(choices=DEPARTMENT, max_length=55)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, related_name='departments')
    
    def __str__(self):
        return self.department
    
    @property
    def get_subject_combo_list(self):
        subject_combo = self.subject_combo.all()
        subject = []
        
        for subj in subject_combo:
            to_string = str(subj)
            subject.append(to_string)
            
            
            subject.sort()
            
        return subject
    
    @property
    def get_similar_course(self):
        '''
          Get similar course will actually work if there's a course that
          has the same subject combination with the course itself
          
          E.g
          Medicine and Surgery ==> [English, Physics, Biology, Chemistry]
          Physiology ==> [English, Physics, Biology, Chemistry]
          Biochemistry ==> [English, Physics, Biology, Chemistry]
          
          For someone with Medicine and Surgery, Biochemistry and Physiology
          will be similar courses.
          
          We need to take note that the course itself is not a similar course
        '''
        department = Department.objects.all()
        similar_department = [] 
        for course in department:
            
            if self.department != str(course):
                
                if self.get_subject_combo_list == course.get_subject_combo_list:
                
                   similar_department.append(course)
               
                
                       
        return similar_department
    
    
    @property
    def if_subject_verified(self):
        get_subject = [subject.is_verified for subject in self.subject_combo.all()]
        if False in get_subject:
            return False
        return True
        
    
    
class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subject_combo')
    subject = models.CharField(choices=SUBJECT, max_length=30)
    is_verified = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.subject
    
    
        


class CutOff(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='cutoff')
    standard = models.FloatField(null=True, blank=True)
    competitiveness = models.IntegerField(null=True, blank=True) # On a scale of 1-10
    quota = models.IntegerField(null=True, blank=True) # the number of admitted student for a course per year
    
    cutoff_2016 = models.FloatField(null=True, blank=True)
    cutoff_2017 = models.FloatField(null=True, blank=True)
    cutoff_2018 = models.FloatField(null=True, blank=True)
    cutoff_2019 = models.FloatField(null=True, blank=True)
    cutoff_2021 = models.FloatField(null=True, blank=True)
    
    # ADD NEW YEARS HERE
    
    
   
    
    predicted = models.FloatField(null=True)
    mean = models.FloatField(null=True, blank=True)
    next_prediction = models.FloatField( null=True, blank=True)
    
    
    def __str__(self):
        return self.department.department
    
    
    
    def save(self, *args, **kwargs):
        
        
                
        
        cutoff_dict = {

            '2016': self.cutoff_2016,
            '2017': self.cutoff_2017,
            '2018': self.cutoff_2018,
            '2019': self.cutoff_2019,
            '2021': self.cutoff_2021,

        }
        
        

        main_cutoff = {}

        cutoffs = []

        for year, cutoff in cutoff_dict.items():
           if cutoff == 0 or cutoff == None:
            pass
           else:
            main_cutoff[year] = cutoff
            

            cutoffs.append(cutoff)
        
                
      
        if not self.competitiveness:
            try:
                self.competitiveness = calculate_competitiveness(cutoffs)
            except:
                pass
            
        if self.mean is None:

            # The non-empty cutoffs are stored in main_cutoff

            list_of_main_cutoffs = list(main_cutoff.values())

            self.mean = np.mean(list_of_main_cutoffs)
        
         
        if self.next_prediction is None:
            year = []
            

            

            for key, value in main_cutoff.items():
                y = int(key)
                year.append(y)
      
        this_year = 2022
        
        
        pred  =linear(year, cutoffs ,this_year)
          
        self.next_prediction = np.mean([self.predicted, self.mean, pred])
         
        super(CutOff, self).save(*args, **kwargs)
      
      
    @property
    def get_cutoff(self):
        
        
        cutoff_dict = {

            '2016': round(self.cutoff_2016,2),
            '2017': round(self.cutoff_2017,2),
            '2018': round(self.cutoff_2018,2),
            '2019': round(self.cutoff_2019,2),
            '2021': round(self.cutoff_2021, 2),
            '2022 Prediction':round( self.next_prediction, 2),

        }

        main_cutoff = {}

        

        for year, cutoff in cutoff_dict.items():
           if cutoff == 0 or cutoff == 'None':
            pass
           else:
            main_cutoff[year] = cutoff
            
        return main_cutoff
        

class Service(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='services/')
    text = models.TextField()
    url = models.CharField(max_length=25)
    number = models.IntegerField(null=True)
    
    class Meta:
        ordering = ['number']
        
    def __str__(self):
        return self.name
    

    