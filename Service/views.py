from django.shortcuts import render
from Company.company import get_quote, get_service, get_department, get_faq, get_fact
from .models import Department
from django.contrib.auth.decorators import login_required




@login_required
def aggregate_predictor(request):
    if request.method == 'POST':
        utme = int(request.POST.get('utme'))
        course_id = request.POST.get('course_id')
        department = Department.objects.get(id=course_id)
        attempts = int(request.POST.get('attempts'))
        
       
        

        from .prediction import predict_aggregate
        try:
       
           aggregate = predict_aggregate(utme, attempts, department)
           
        except:
            error = {
                'error': f'Algorithm does not accept {utme}. Enter a valid UTME Score',
                'department': get_department(),
            }
            return render(request, 'service/aggregate-predictor.html', error)
            
        
        
        
        
        
        
        context = {
            'aggregate': round(aggregate, 2),
            'department':department,
            'quote': get_quote(),
            'services': get_service(),
            'faq': get_faq(),
            'fact': get_fact(),
            
        }
        
        
        
        
        
        
        return render(request, 'service/aggregate-predictor-result.html', context)
        
        
    context = {
        'department': get_department(),
    }
    return render(request, 'service/aggregate-predictor.html', context)

@login_required
def chance_calculator(request):

    if request.method == 'POST':
        utme = int(request.POST.get('utme'))
        course_id = request.POST.get('course_id')
        
        

        
            

        #let's query the department from the database
        
        try:   
           from .prediction import predict_chance, return_status
           department = Department.objects.get(id=course_id)
           chance = predict_chance(utme, course_id)
           status = return_status(chance)
               
           get_similar_course_chance = department.get_similar_course
           dic_of_similar_course = {}
           
           for course in get_similar_course_chance:
               similar_chance = predict_chance(utme, course.id)
               dic_of_similar_course[course] = similar_chance
           similar_course = dic_of_similar_course
       
           
           

        except Exception as error:
            
            context = {
                'error': error,
                'department': get_department(),
            }
            return render(request, 'service/chance-calculator.html', context)
        
        result_content = 'I just used the chnace caculator to predict my chnace of gaining admission into University of Ibadan. It was really awesome'
        
        context = {
            'chance': chance,
            'department': department,
            'similar': similar_course,
            'status': status,
            'services': get_service(),
            'quote': get_quote(),
            
            'faq': get_faq(),
            'fact': get_fact(),
            
            
            }
        
           
        
            

        return render(request, 'service/chance-calculator-result.html', context)  
            
        
        
    context = {
        'department': get_department(),
    }
        
    return render(request, 'service/chance-calculator.html', context)

@login_required
def cutoff_tracker(request):

    if request.method == 'POST':

        course_id = request.POST.get('course_id')
        
        try: 
            department = Department.objects.get(id=course_id)
            cutoff = department.cutoff
            
            
        except:
            error = 'We do not have any cutoff marks for this course'
            context = {
                'error_message': error,
                'department': get_department(),
            }
            return render(request, 'service/cutoff-tracker.html', context)
        context = {


            'cutoff': cutoff,
            'department': department,
            'quote': get_quote(),
            'services': get_service(),
            'faq': get_faq(),
            'fact': get_fact(),
            }

        return render(request, 'service/cutoff-tracker-result.html', context)
    context = {
        'department': get_department(),
    }
    return render(request, 'service/cutoff-tracker.html', context)

@login_required
def subject_checker(request):

    if request.method == 'POST':

        course_id = request.POST.get('course_id')
        print(course_id)
        

        try:
            dep = Department.objects.get(id=course_id)
            
        except:
            error_message = 'We are not sure of the right subject combination for this course'
            
            
            return render(request, 'service/subject-combo-checker.html', {'error_message': error_message, 'department': get_department(),})
            
        
        
        context = {
            'department': dep,
            'subject': dep.get_subject_combo_list,
            'is_verified' : dep.if_subject_verified,
            
            'quote': get_quote(),
            'services': get_service(),
            'faq': get_faq(),
            'fact': get_fact(),
            
                       
        }

        return render(request, 'service/subject-combo-checker-result.html', context)
    context = {
        'department': get_department(),
    }
    return render(request, 'service/subject-combo-checker.html', context)



