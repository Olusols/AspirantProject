from django.core.exceptions import ValidationError
import pandas as pd
import numpy as np
from statistics import mean
from Service.data import Data


'''

Prediction will be hence forth looped from the database

Predict Chance : UTME Performance, Nature of Course, Course Competitiveness, 
     Number of Student to be admitted(quota) Vs.
     Number of students registered(from the academic detail database that are aspirants actually)
     
     If not aspirant in acadmic detail, we save from the academic detail


'''


def return_status(chance):
        
        if chance >= 51 and chance < 55:
            return 'Worse'
        elif chance >= 55 and chance < 68:
            return 'Bad'
        elif chance >= 68 and chance < 75:
            return 'Good'
        elif chance >= 75 and chance < 82:
            return 'Very Good'
        else:
            return 'Excellent'
        
        
def competitiveness_range(number):
    if number < 50:
        raise ValueError('Number cannot be less than 50')
    if number > 50 and number <= 55:
        comp = 3
    elif number > 55 and number <= 58:
        comp = 4
    elif number > 58 and number <= 60:
        comp = 5
    elif number > 60 and number <= 63:
        comp = 6
    elif number > 63 and number <= 68:
        comp = 7
    elif number > 68 and number <= 70:
        comp = 8
    elif number > 70 and number <= 73:
        comp = 9
    else:
        comp=10 
        
    return comp

def calculate_competitiveness(list_of_main_cutoffs):
    lists = sorted(list_of_main_cutoffs)
    three_highest_list = lists[-3:]
    if 0 in three_highest_list:
        raise ZeroDivisionError('0 is part of the three highest')
    mean_list = mean(three_highest_list)
    value = competitiveness_range(mean_list)
    return value


def linear(x, y, utme):
    from scipy import stats
    from math import ceil
    try:
    
       linear_model = stats.linregress(x, y)
       result = linear_model.slope * utme + linear_model.intercept
       
    except:
        return ValidationError('You have to have more than one data point in your list')
    
    return ceil((result))   
    


def predict_aggregate(utme, number, course):
    
    if utme < 200 or utme > 400:
        raise ValidationError(f'{utme} greater than 400 or less than 200')
    
    data = Data.objects.all()
    
    #all the data
    all_utme = [d.utme for d in data]
    all_putme = [d.putme for d in data]

    # 2018 data
    
    utme_2018 = [d.utme for d in data if d.year_of_admission==2018]
    putme_2018 = [d.putme for d in data if d.year_of_admission==2018]
 
    #number of attempts
    if number >3:
        number = 3
    utme_attempts = [d.utme for d in data if d.number_of_attempts==number]
    putme_attempts = [d.putme for d in data if d.number_of_attempts==number]
  
    data_attempts = linear(utme_attempts, putme_attempts, utme)

    data_2018 = linear(utme_2018, putme_2018, utme)

    all_data = linear(all_utme, all_putme, utme)
    
    
    
    #department
    try:
       utme_depart = [d.utme for d in data if d.department==course]
       putme_depart = [d.putme for d in data if d.department==course]
       
       
       
       data_depart = linear(utme_depart, putme_depart, utme)
        

       mean_data = mean(
            [data_attempts, all_data, data_depart, data_2018])
       
       
       
    
    except:
       mean_data = mean([data_attempts, all_data, data_2018])
       
    aggregate = utme/8 + mean_data/2
       
    return aggregate
    
    



def predict_chance(utme,department):
    
    '''
      To predict the chance of gaining admission
        UTME ==> 0.7
        Nature of course(standards) ==> 0.1
        Course Competitiveness ==> 0.1 Table: Department Table
        Number of student registered(from AspirantData table) Vs. Admission quota(Department table) ==> 0.1
        
        
    '''
    if utme < 200 or utme >400:
        raise ValueError('Algorithm fail to predict chance')
    
    from Service.models import Department
    
        
    cutoff = Department.objects.get(id=department).cutoff
    
    standard = cutoff.standard
    quota = cutoff.quota
    competitiveness = cutoff.competitiveness
    next_prediction = cutoff.next_prediction
    

   
    utme_convert = utme/4

    if utme_convert < next_prediction:
        if next_prediction - utme_convert >= 5:
                   chance = 55
        elif (next_prediction - utme_convert >=4  ):
                   chance = 60
        elif (next_prediction - utme_convert >= 3 ):
                   chance = 65
        elif (next_prediction - utme_convert >= 2 ):
                   chance = 70
            
        else:
                   chance = 74
    elif utme_convert > next_prediction:
               if  utme_convert - next_prediction <= 2:
                   chance = 77
               elif  utme_convert - next_prediction <=3:
                   chance = 80
               elif utme_convert - next_prediction <= 4:
                   chance = 85
               else:
                   chance = 90
               
    else:
               chance = 73
    
    calc = (10 - competitiveness)*.05 + chance*.9 + standard*.05
    from math import ceil
    return ceil(calc)
            

def calculate_putme_score(utme, course_id):
    from Service.models import Department
    cutoff = Department.objects.get(id=course_id).cutoff
    next_prediction = cutoff.next_prediction
    if next_prediction < 55:
        pred = 55
    elif next_prediction >55 and next_prediction <= 60:
        pred = 60
    elif next_prediction > 60 and next_prediction <= 65:
        pred = 65
    elif next_prediction >65 and next_prediction <=70:
        pred = 70
    elif next_prediction >70 and next_prediction <= 75:
        pred = 75
    else:
        pred = 80

    putme_score = (8*(pred) - utme)/4
    if putme_score < 60:
        putme_score = 60
    elif putme_score > 90:
        putme_score = 90
    from math import ceil
    return ceil(putme_score)


