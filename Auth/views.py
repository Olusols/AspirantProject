from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Company.company import get_state, get_department
from .auth import  get_username_or_email, check_email_and_username,check_password, check_password_match, get_whatsapp_link


def register(request):
   if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')   
        
        try:
            if check_email_and_username(email, username):
                if check_password(password1):
                    if check_password_match(password1, password2):
                        from django.contrib.auth import login
                        user  = User.objects.create(username=username, email=email)
                        user.set_password(password1)
                        user.save()
                        authenticate(username=username, password=password1)
                        login(request, user)
                        return redirect("user-detail")               
        except Exception as error:
            context = {
                'error_message': error,
            }
            return render(request, "auth/register.html", context)
   return render(request=request, template_name="auth/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        try:
            user_id = get_username_or_email(username)
            get_user = User.objects.get(pk=user_id)
            
            from django.contrib.auth import login
            if get_user.check_password(str(password)):
                login(request, get_user)
                return redirect('index')
            raise ValueError('Password did not match')
            
            
        except Exception as error:
            context = {
                'error_message': error,
            }
            return render(request, "auth/login.html", context)
    return render(request=request, template_name="auth/login.html")
            

class Login(LoginView):
    template_name = 'auth/login.html'

    
class Logout(LogoutView):
    template_name = 'auth/logout.html'
    next_page = 'auth:login'
    
def welcome(request):
    return render(request, 'auth/welcome.html')

def user_detail(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        course = request.POST.get('course')
        utme_attempts = request.POST.get('utme_attempts')
        whatsapp = request.POST.get('whatsapp')
        tutorial = request.POST.get('tutorial')
        know_about_us = request.POST.get('know_about_us')
        state = request.POST.get('state')
        
        print(first_name, last_name, course, utme_attempts, whatsapp, tutorial, know_about_us, state)
        
        # first_name, last_name ==> save to user
        from django.contrib.auth.models import User
        if request.user.is_authenticated:
         try:
           user = User.objects.get(username=request.user.username)
        
           user.first_name = first_name
           user.last_name = last_name
           user.save()
         except:
             pass
        
        
       
        
        
        from Auth.models import UserDetail
        if request.user.is_authenticated:
         
          try:
           
            if get_whatsapp_link(whatsapp):
            
             personal = UserDetail(
                user=request.user,
                utme_attempts=utme_attempts,
                whatsapp=get_whatsapp_link(whatsapp),
                is_attending_tutorial=tutorial,
                state=state,
                course=str(course),
                
                know_about_us=know_about_us,
            )
                
        
            personal.save()
          except Exception as error:
               context = {
                   'error_message': error,
               }
               return render(request, 'auth/user-detail.html', context)
            
        return redirect('welcome')
        
        
    context = {
        'state': get_state(),
        'department': get_department,
    }
    return render(request, 'auth/user-detail.html', context)