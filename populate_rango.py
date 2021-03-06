import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foreign_with_django.settings')
import django
django.setup()
from Foreign_App.models import *

import pandas as pd


def populate():
    python_pages = [
        {"title":"Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial"},
        {"title":"how to think like a computer scientist",
         "url":"http://www.greenteapress.com/thinkpython"},
        {"title":"Learn Python in 10 minutes",
         "url":"http://www.korokithakis.net/tutorials/python"}
    ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01"},
        {"title":"django rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"how to tango with django",
         "url":"http://www.tangowithdjango/"},
    ]

    other_pages = [
        {"title":"bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"flask",
         "url":"http://flask.pocoo.org"},
    ]

    cats = {"Python":{"pages":python_pages},
            "Django":{"pages":django_pages},
            "Other Framworks":{"pages":other_pages},}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print (" - {0} - {1}".format(str(c),str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    if c.name == "Python":
        c.views=128
        c.likes=64
    elif c.name == "Django":
        c.views = 64
        c.likes = 32
    elif c.name == "Other Framworks":
        c.views = 32
        c.likes = 16
    c.save()
    return c


def populateforeign():
    pf0 = pd.read_excel('data.xlsx')
    for index, row in pf0.iterrows():
        p0 = PersonalInformation.objects.get_or_create(tel=row['tel'])[0]
        p0.name = row['name']
        p0.tel = row.tel
        p0.email = row.email
        p0.gender = row.gender
        p0.department = row.department
        p0.ID_num = row.ID_num
        p0.Place_of_Birth = row.place_birth
        p0.Date_of_Birth = row.date_birth #pd.Period(row['date_birth'],freq='D')
        p0.duty = row.duty
        p0.identity = row.identity
        p0.race = row.race
        p0.political_identity = row.political_identity
        p0.securety = row.securety
        p0.status_health = row.status_health
        p0.emergency_contact_name = row.emergency_contact_name
        p0.emergency_contact_tel = row.emergency_contact_tel
        p0.sign = row['name']+'-'+row.place_birth+'-'+row.date_birth.strftime('%Y-%m-%d')
        p0.save()
        print(" %d person is saved" %(index))
    return


def pupulate_passport():
    pf1 = pd.read_excel('data.xlsx', sheetname=[1])
    for p0 in PersonalInformation.objects.all():
        for index1, row1 in pf1[1].iterrows():
            if p0.name == row1['name']:
                p1 = PassportInformation.objects.get_or_create(person=p0, passport_number=row1['passport_number'])[0]
                p1.passport_number = row1['passport_number']
                p1.date_issue = row1.date_issue
                p1.date_expire = row1.date_expire
                p1.issue_office = row1.issue_office
                p1.issue_place = row1.issue_place
#                if row1.date_out == '':
#                    p1.date_out = row1.date_issue
#                else:
#                    p1.date_out = row1.date_out
#                if row1.date_back == '':
#                    p1.date_back = row1.date_issue
#                else:
#                    p1.date_back = row1.date_back
                p1.save()
                print(" %d passports are saved" % (index1))
    return


def populate_visa():
    pf2 = pd.read_excel('data.xlsx', sheetname=[2])
    for p1 in PassportInformation.objects.all():
        for index2, row2 in pf2[2].iterrows():
            if p1.passport_number == row2['passport_number']:
                p2 = VisaInformation.objects.get_or_create(passport_number=p1,country=row2.country,issue_date=row2.issue_date)[0]
                p2.passport_number = row2['passport_number']
                p2.country = row2.country
                p2.issue_date = row2.issue_date
                p2.expire_date = row2.expire_date
                p2.visa_type = row2.visa_type
                p2.visa_sign = p2.passport_number+'-'+row2.country+'-'+row2.issue_date.strftime('%Y-%m-%d')
                #p2.visafile = row2.visafile
                p2.save()
                print(" %d visas are saved" % (index2))
    return


def populate_country_city():
    pf = pd.read_excel('fee.xlsx')
    for index, row in pf.iterrows():
        p3 = CountryInformation.objects.get_or_create(name=row.country)[0]
        p3.name = row.country
        if row.cash == '美元':
            p3.cash = 1
        elif row.cash == '欧元':
            p3.cash = 2
        elif row.cash == '英镑':
            p3.cash = 3
        elif row.cash == '日元':
            p3.cash = 4
        p3.save()
        p4 = CityInformation.objects.get_or_create(country=p3,city=row.city)[0]
        if row.city=='':
            p4.city = '所有城市'
        else:
            p4.city = row.city
        p4.short_accom = row.short_accom
        p4.short_meal = row.short_meal
        p4.short_work = row.short_work
        p4.save()
        print(" %d cities are saved" % (index))



if __name__ == '__main__':
    print ("Starting Rango population script ...")
    populate()
    populateforeign()
    pupulate_passport()
#    populate_visa()
    populate_country_city()



