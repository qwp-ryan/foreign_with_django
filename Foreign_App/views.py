# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from .models import Category, Page
from .models import PassportInformation, VisaInformation, PersonalInformation
from .forms import PassportInformationForm, VisaInformationForm, PersonalInformationForm
from .forms import CategoryForm, PageForm
from .forms import UserForm, UserProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime


def delegationprocess(Request, delegation_sign):
    # 这个view想要把一个团组的整个申请填报流程都展现出来，每一步的信息全都表现出来。
    context_dict = {}
    names = []
    passport = []
    country_names = []
    members = []

    try:
        Deleg = Delegation.objects.get(sign=delegation_sign)
        for men in Deleg.Members.all():
            names.append(men.name)
        for countries in Deleg.country.all():
            country_names.append(countries.name)

        # members.append(Delegation.Members.objects.filter())
        #        for members in Deleg.Members:
        #            passport.append(PassportInformation.object.filter(person=members))
        #        visa = VisaInformation.object.filter(Passport=passport)
        permission = Permission.objects.filter(delegation=Deleg)
        budget = BudgetInformation.objects.filter(delegation=Deleg)
        summary = SummaryInformation.object.filter(delegation=Deleg)

        #        context_dict['Passport'] = passport
        #        context_dict['Visa'] = visa
        context_dict['Permision'] = permission
        context_dict['Budget'] = budget
        context_dict['Summary'] = summary

    except Delegation.DoesNotExist:
        context_dict['delegation'] = None
    return render(Request, 'rang/category_2.html', context_dict)


def ShowDelegation(Request):#这个view要把所有的团组列出来，普通人只能看到自己参加的和自己填报的团组情况
    Delegation_list = Delegation.objects.order_by('-time_leave')[:]

#    Delegation_list = Delegation.objects.all(Delegation.time_leave-timezone.now)
    context_dict = {'delegations': Delegation_list}
    response = render(Request, 'rang/index_2.html', context_dict)
    return response


def index(Request):
#    Request.session.set_test_cookie()
    category_list = Category.objects.order_by('-likes')[:5]
    page_list=Page.objects.order_by('-views')[:5]
    context_dict={'categories':category_list,'pages':page_list}
    response=render(Request,'rang/index_1.html',context_dict)
    visitor_cookie_handler(Request,response)
    return response

#    return render(Request, 'rang/index_1.html', context = context_dict)
#    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About </a>")

def about(Request):
    if Request.session.test_cookie_worked():
        print ("TEST COOKIE WORKED!")
        Request.session.delete_test_cookie()

    print(Request.method)
    print(Request.user)
    context_dict={'newmessage': "about page of Django!"}
    #return render(Request, 'rang/about.html', context = context_dict)
    return render(Request, 'rang/about_1.html', context=context_dict)

    #return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'> Index </a>")


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug = category_name_slug)
        pages = Page.objects.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request,'rang/category_1.html',context_dict)


def add_category(request):
    form=CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat=form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request,'rang/add_category_1.html',{'form':form})


def add_page(request, category_name_slug):
    try:
        category=Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None


    form=PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page=form.save(commit=False)
                page.category=category
                page.views=0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict={'form': form, 'category':category}
    return render(request,'rang/add_page_1.html',context_dict)


def add_Project(request):
    form=CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat=form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request,'rang/add_category_1.html',{'form':form})

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,
                  'rang/register.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Rango account is disabled")
        else:
            print("Invalid login details:{0},{1}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'rang/login.html',{})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def visitor_cookie_handler(request,response):
    visits=int(request.COOKIES.get('visit','1'))

    last_visit_cookie=request.COOKIES.get('last_visit',str(datetime.now()))
    last_visit_time=datetime.strptime(last_visit_cookie[:-7],
                                      '%Y-%m-%d %H:%M:%S')
    if(datetime.now()-last_visit_time).days>0:
        visits = visits+1
        response.set_cookie('last_visit',str(datetime.now()))
    else:
        visits = 1
        response.set_cookie('last_visit',last_visit_cookie)

    response.set_cookie('visits',visits)


def person_index(Request):
    Person_list = PersonalInformation.objects.all()
    context_dict = {'Persons':Person_list}
    response = render(Request,'rang/Person_list.html',context_dict)
    return response


def add_person(Request):
    form = PersonalInformationForm()
    if Request.method == "POST":
        form = PersonalInformationForm(Request.POST)
        if form.is_valid():
            form.save(commit=True)
            return person_index(Request)
        else:
            print(form.errors)
    return render(Request, 'rang/add_person.html',{'form':form})


def person_detail(Request, person_sign):
    person = PersonalInformation.objects.filter(sign=person_sign).values()
    return render(Request, 'rang/detail.html', {'person':person}, person_sign)


def show_visa(Request, person_sign):
    form = PersonalInformationForm()

    if Request.method == 'POST':
        form = CategoryForm(Request.POST)

        if form.is_valid():
            form.save(commit=True)
            return person_index(Request)
        else:
            print(form.errors)

    return render(Request, 'rang/add_person.html', {'form': form})



def add_passport(Request, person_sign):
    try:
        person=PersonalInformation.objects.get(sign=person_sign)# 不唯一，希望使用姓名，生日，出生地三者同时作为评价标准
    except PersonalInformation.DoesNotExist:
        person = None
    form = PassportInformationForm()
    if Request.method == 'POST':
        form = PassportInformationForm(Request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(Request)
        else:
            print(form.errors)
    return render(Request, 'rang/add_passport.html',{'form':form})



def show_passport(request, Id_num):
    context_dict = {}
    try:
        person = PersonalInformation.objects.get(Id_num=Id_num)
        passports = PassportInformation.objects.filter(person=person)
        context_dict['passports'] = passports
        context_dict['person'] = person
    except person.DoesNotExist:
        context_dict['passport'] = None
        context_dict['visas'] = None
    return render(request,'rang/passport.html', context_dict)

def show_visa(request, passport_number):
    context_dict = {}
    try:
        passport = PassportInformation.objects.get(passport_number=passport_number)
        visas = VisaInformation.objects.filter(passport=passport)
        context_dict['visas'] = visas
        context_dict['passport'] = passport
    except passport.DoesNotExist:
        context_dict['passport'] = None
        context_dict['visas'] = None
    return render(request,'rang/passport.html', context_dict)





def add_visa(request, passport_number):
    try:
        passport=PassportInformation.objects.get(pussport_number=passport_number)
    except passport.DoesNotExist:
        passport = None
    form = VisaInformationForm()
    if request.method == 'POST':
        form = VisaInformationForm(request.POST)
        if form.is_valid():
            if passport:
                visa=form.save(commit=False)
                visa.passport_number=passport_number
                visa.save()
                return show_passport(request, passport_number)
        else:
            print(form.errors)
    context_dict={'form': form, 'passport':passport}
    return render(request,'rang/add_visa.html',context_dict)


from .New_view import *