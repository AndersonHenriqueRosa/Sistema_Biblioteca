from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Users
from hashlib import sha256
# Create your views here.s

def login(request):
    status = request.GET.get('status')
    return render(request,'user/login.html', {'status': status})

def registration(request):
    status = request.GET.get('status')
    return render(request, 'user/registration.html',{'status': status})

def validate_registration(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = Users.objects.filter(email = email)
    
    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/registration/?status=1')
    
    if len(password) < 8:
        return redirect('/auth/registration/?status= 2')
    
    if len(user) > 0:
        return redirect('/auth/registration/?status=3')
    
    try:
        password = sha256(password.encode()).hexdigest()
        user = Users(name = name, email = email, password = password)
        user.save()
        return redirect('/auth/registration/?status=0')
        
    except:
        return redirect('auth/registration/?status=4')   
    
def  validate_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = sha256(password.encode()).hexdigest()
    user = Users.objects.filter(email = email).filter(password = password)
    if len(user) == 0:
        return redirect('/auth/login/?status=1')
    elif len(user) == 1:
        request.session['user'] = user[0].id
        return redirect('/book/home')
        
    return HttpResponse(f"{email} {password}")

def logout(request):
    request.session.flush()
    return redirect('/auth/login')