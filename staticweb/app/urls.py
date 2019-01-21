"""staticweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('faculty/cse',views.cse,name='cse'),
path('faculty/ece',views.ece,name='ece'),
path('faculty/mech',views.mech,name='mech'),
path('faculty/eee',views.eee,name='eee'),
path('faculty/prod',views.prod,name='prod'),
path('faculty/bio',views.bio,name='bio'),
path('faculty/arch',views.arch,name='arch'),
path('faculty/phy',views.phy,name='phy'),
path('faculty/mat',views.mat,name='mat'),
path('faculty/pharm',views.pharm,name='pharm'),
path('faculty/remote',views.remote,name='remote'),
path('faculty/space',views.space,name='space'),
path('faculty/manage',views.manage,name='manage'),
path('faculty/hotel',views.hotel,name='hotel'),
path('faculty/chem',views.chem,name='chem'),
path('faculty/chemeng',views.chemeng,name='chemeng'),
path('faculty/civil',views.civil,name='civil'),

path('transport/autodirectory',views.autodirectory,name='autodirectory'),
path('transport/busdirectory',views.busdirectory,name='busdirectory'),
path('transport/rentals',views.rentals,name='rentals'),


path('shops/canteens',views.canteens,name='canteens'),
path('shops/tailor',views.tailor,name='tailor'),
path('shops/stationary',views.stationary,name='stationary'),



path('Administration',views.Administration),


path('home',views.home,name='home'),


]
