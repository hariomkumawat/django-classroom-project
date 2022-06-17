from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from members.models import *

from members.models import Join_class

# Create your views here.

def cover(request):
    return render(request,'cover.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def registerview(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request,'register.html')


def logoutview(request):
    logout(request)
    return render(request,'logout.html')

def home(request):
    return render(request,'home.html')

def create_class(request):
    if request.method == 'POST':
        Create_class.objects.create(
            class_id = request.POST['class_id'],
            class_name = request.POST['class_name'],
            subject_code = request.POST['subject_code'],
            branch_code = request.POST['branch_code'],
            college_code = request.POST['college_code']
        )
        return redirect('pop_joinclass')
    return render(request,'createclass.html')

def pop_joinclass(request):
    if request.method == 'POST':
        pop = Create_class.objects.filter(subject_code='subject_code',branch_code='branch_code',college_code='college_code')
        if pop:
            return redirect('joinroom.html',{'pop':pop})
    return render(request,'pop_joinclass.html')

def join_room(request):
    get_all = Join_class.objects.all()
    if request.method == 'POST':
        Join_class.objects.create(
            class_id = request.POST['class_id'],
            user_id = request.user.id
        )
        return render(request,'joinroom.html',{'get_all':get_all})
    return render(request,'joinroom.html')