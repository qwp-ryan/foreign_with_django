"""my_rango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='Foreign_App'
urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),

    url(r'^$',views.index, name='index' ),
    url(r'^index/',views.ShowDelegation, name='index' ),
    url(r'^delegation/(?P<delegation_sign>[\w\-]+)/$',views.delegationprocess,name='delegationprocess'),

    url(r'^add_person/$',views.add_person, name='add_person'),
    url(r'^person_list/(?P<persion_sign>[\w\-]+)/add_passport/$',views.add_passport, name='add_passport'),
    url(r'^person_list/(?P<persion_sign>[\w\-]+)/(?P<passport_number>[\w\-]+)$',views.add_visa, name='add_visa'),

    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/',views.user_logout, name='logout'),
]#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
