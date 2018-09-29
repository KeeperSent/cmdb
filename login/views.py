from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
from mysite import settings
import datetime

# Create your views here.

import hashlib


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('loged', None):
        return redirect('/index/')
    if request.method == 'POST':
        f_login = forms.F_User(request.POST)
        message = 'invalid input'
        if f_login.is_valid():
            username = f_login.cleaned_data.get('username')
            password = f_login.cleaned_data.get('password')
            # ....
            try:
                user = models.M_User.objects.get(name=username)
            except:
                message = 'not exist'
                return render(request, 'login/login.html', locals())


            if user.password == hash_code(password):
                request.session['loged'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = 'wrong passwd'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    f_login = forms.F_User()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('loged', None):
        return redirect('/index/')

    if request.method == "POST":
        f_reg = forms.F_Reg(request.POST)
        message = 'invalid input'
        if f_reg.is_valid():
            username = f_reg.cleaned_data['username']
            password1 = f_reg.cleaned_data['password1']
            password2 = f_reg.cleaned_data['password2']
            email = f_reg.cleaned_data['email']
            sex = f_reg.cleaned_data['sex']
            if password1 != password2:
                message = 'wrong passwd'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.M_User.objects.filter(name=username)
                if same_name_user:
                    message = 'user existed'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.M_User.objects.filter(email=email)
                if same_email_user:
                    message = 'email existed'
                    return render(request, 'login/register.html', locals())


            new_user = models.User()
            new_user.name = username
            new_user.password = hash_code(password2)
            new_user.email = email
            new_user.sex = sex
            new_user.save()


    f_reg = forms.F_Reg()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('loged', None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')


