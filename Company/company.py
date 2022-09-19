from Service.models import Department

current_session = '2022/2023'

def get_department():
    '''
      get all the department in alphabetical order
      To be used in forms(Predict Aggregate, Predict Chance
      Subject Combination, Check Cutoff, Personal Detail form and models and many more)
    '''
    department = Department.objects.order_by('department')
    return department

def get_state():
    from .models import State
    state = State.objects.order_by('state')
    return state

def UTME_checker(utme):
    if utme < 200 or utme > 400:
        raise ValueError(f'University of Ibadan does not accept {utme}')
    return True

def PUTME_checker(putme):
    if putme < 50 or putme > 100:
        raise ValueError(f'Algorithm fails to accept {putme} as your Post UTME Score')
    return True

def get_quote():
    from .models import Quote
    import random
    quote = random.choice(list(Quote.objects.all()))
    return quote


def get_service():
    from Service.models import Service
    service = Service.objects.order_by('number')
    return service