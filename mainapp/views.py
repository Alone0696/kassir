from ctypes.wintypes import WPARAM
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import * 
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


import locale

from mainapp.models import Cash
from mainapp.forms import LoginForm


def logout_user(request):
    logout(request)
    return redirect('login')

def calc(type,date):
    sum = 0
    sum_n = 0
    sum_b = 0
    nal = Cash.objects.filter(type=type).filter(date__date=date).filter(beznal=False)
    beznal = Cash.objects.filter(type=type).filter(date__date=date).filter(beznal=True)
    
    for i in nal:
        sum_n+=i.price
    for i in beznal:
        sum_b+=i.price
    
    sum = sum_n+sum_b
    mass = [sum,sum_n,sum_b]
    return mass
    
@login_required(login_url="login")
def main(request):
    mass = [0,0,0]
    s_z = 0
    t = Cash.objects.all()
    if request.method == "POST":
        if request.POST.get("type") == "Касса":
            mass = calc("Касса",request.POST.get("date"))
        if request.POST.get("type") == "Закупка":
            s = Cash.objects.filter(type="Закупка").filter(date__date=request.POST.get("date"))
            for i in s:
                s_z+=i.price
    context = {
        "all":t,
        "s_k":mass[0],
        "s_k_n":mass[1],
        "s_k_b":mass[2],
        "s_z":s_z,
    }
    return render(request,"main.html",context=context)

@login_required(login_url="login")
def get_kassa(request):
    all = Cash.objects.filter(type="Касса").filter(date__date = request.GET.get("date"))
    mass = calc("Касса",request.GET.get("date"))
    context = {
        "date":request.GET.get("date"),
        "all":all,
        "s_k":mass[0],
        "s_k_n":mass[1],
        "s_k_b":mass[2],
    }
    return render(request,"get_kassa.html",context=context)

@login_required(login_url="login")
def kassa(request):
    if request.method == "POST":
        item = request.POST.get("item")
        price = request.POST.get("price")
        beznal = request.POST.get("beznal")
        if beznal == None:
            beznal = False
        else:
            beznal = True
        s = Cash(item=item,price=price,type="Касса",beznal=beznal)
        s.save()
        return HttpResponseRedirect(request.path)
    t = Cash.objects.filter(type="Касса").filter(date__date=datetime.today().date())
    s = 0
    for i in t:
        s+=i.price
    locale.setlocale(locale.LC_TIME,"ru_RU")
    date = datetime.today().date().strftime('%d %B %Y')
    context = {
        "all":t,
        "s":s,
        "date":date,
    }
    return render(request,"kassa.html",context=context)

@login_required(login_url="login")
def zakupki(request):
    if request.method == "POST":
        item = request.POST.get("item")
        price = request.POST.get("price")
        s = Cash(item=item,price=price,type="Закупка")
        s.save()
        return HttpResponseRedirect(request.path)
    t = Cash.objects.filter(type="Закупка").filter(date__date=datetime.today().date())
    s = 0
    for i in t:
        s+=i.price
    locale.setlocale(locale.LC_TIME,"ru_RU")
    date = datetime.today().date().strftime('%d %B %Y')
    context = {
        "all":t,
        "s":s,
        "date":date,
    }
    return render(request,"zakupki.html",context=context)

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    next_page = "/"

