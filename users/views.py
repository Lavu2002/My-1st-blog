from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
import re
regex1=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
regex2=re.compile('[A-Z]')
regex3=re.compile('[a-z]')
regex4=re.compile('[0-9]')

def register(request):
    print("register 1")
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']



        
        if len(username)>8:
            messages.error(request,"Username must be under 8 characters")
            return render(request,'users/register.html')
        elif not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return render(request,'users/register.html')
        elif(regex1.search(password1)==None or regex2.search(password1)==None or regex3.search(password1)==None or regex4.search(password1)==None):
                messages.error(request,"Password must contain one uppercase, one lowercase,one digit and one special character")
                return render(request,'users/register.html')
        elif(regex1.search(password2)==None or regex2.search(password2)==None or regex3.search(password2)==None or regex4.search(password2)==None):
                messages.error(request,"Password must contain one uppercase, one lowercase,one digit and one special character")
                return render(request,'users/register.html')
            
        else:
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Already taken")
                    return redirect(request.POST.get('next'))
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Exists")
                    return redirect('/users/register')
                else:
                    user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    # send_email(request, user)
                    messages.info(request, 'User Created Successfully')
                    auth.login(request,user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        
                        return redirect('/')
            else:
                messages.info(request, "Password didn't match")
                print("register 4")
                return redirect('/users/register')

    else:
        return render(request,'users/register.html')

   


def login(request):
   

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("succesfully login 2")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')

        
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'users/login.html')

    else:
        return render(request, 'users/login.html')


def logout(request):
    print("successfully logout")
    auth.logout(request)
    
    return redirect('/')

def send_email(request, user):
    """
    Send an welcome email to the user.
    When a user registers a welcome email is sent
    to the email address they registered with
    """

    subject = "Thank you for registering and Welcome to Rynkbell."
    message = """Hi %s,\n\n  
              Welcome to rynkbell!\n\n
              On Rynkbell Site you will be able to:\n
              - See all rynkbell youtube mod videos in one place\n
              - Open support tickets if you need technical help\n
              - Visit, comment and vote in our blog\n
              - Avail the latest offers and discounts\n
              - And much more...\n\n\n
              Looking forward to see you around\n\n
              Kind regards\n rynkbell Team""" % user.first_name

    from_email = "lavanyapatial@gmail.com"
    send_mail(subject, message, from_email, [user.email])


def contact(request):
    print(contact)

