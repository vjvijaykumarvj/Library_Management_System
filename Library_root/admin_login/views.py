from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def Register(request):
    if request.method == 'GET':
        return render(request,'admin_login/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # validation parts starts here
        if username == '' or password == '' or email == '' or cpassword == '':
            messages.error(request, 'Mandatary fields are missing please check')
            return render(request,'admin_login/register.html')
        # password and c password are matching are not cheking
        if password != cpassword:
            messages.error(request, 'Password and conform password are not matching')
            return render(request,'admin_login/register.html')
        # user already exists Give the error messege
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return render(request,'admin_login/register.html')
        # emalil id already exists give the erroe messege
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists ')
            return render(request,'admin_login/register.html')
        # if there is no errors go to login page
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            # save the data and go to login page
            return redirect('/login/')
def Login(request):
    if request.method == 'GET':
        return render(request,'admin_login/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            #redirct to home page
            return redirect('/home/')
        else:
            messages.error(request,'username password incorrect ')
            return redirect('/login/')
def Logout(request):
    logout(request)
    #redirct to again login page
    return redirect('/login/')


