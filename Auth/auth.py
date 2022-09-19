from django.contrib.auth.models import User

def get_username_or_email(detail):
    #return user.id
    user = User.objects.all()
    
    if user.filter(username=detail).exists():
        id = user.get(username=detail).id
        return id
    elif user.filter(email=detail).exists():
        id = user.get(email=detail).id
        return id
    raise User.DoesNotExist(f'{detail} does not exist in the database')
        
def check_email_and_username(email, username):
    user = User.objects.all()
    
    
    if user.filter(email=email).exists():   
       raise User.DoesNotExist(f'{email} has already existed in the database')
    
    if user.filter(username=username).exists():
        raise User.DoesNotExist(f'{username} has already existed in the database')
    
    
    return True

def check_password(password):
    '''
      This helps to check the length of a password
    '''
    
    if len(password) < 8:
        raise ValueError('Password must be atleast 8 characters')
    return True

def check_password_match(password1, password2):
    if password1 != password2:
        raise ValueError('Password does not match. Please check and try again')
    return True


def get_whatsapp_link(whatsapp):
    if len(str(whatsapp)) != 11:
        raise ValueError('Your whatsApp number may not be correct. Please check and try again')
    stripped_whatsapp = whatsapp.lstrip('0')
    whatsapp_link = f'https://wa.me/234{stripped_whatsapp}'
    return whatsapp_link

