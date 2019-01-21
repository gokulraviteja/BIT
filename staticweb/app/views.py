from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"app/home.html")
def cse(request):
    return render(request,"app/cse.html")
def ece(request):
    return render(request,"app/ece.html")
def mech(request):
    return render(request,"app/mech.html")
def eee(request):
    return render(request,"app/eee.html")
def bio(request):
    return render(request,"app/bio.html")
def phy(request):
    return render(request,"app/phy.html")
def mat(request):
    return render(request,"app/mat.html")
def arch(request):
    return render(request,"app/arch.html")
def prod(request):
    return render(request,"app/prod.html")
def chem(request):
    return render(request,"app/chem.html")
def chemeng(request):
    return render(request,"app/chemeng.html")
def civil(request):
    return render(request,"app/civil.html")
def hotel(request):
    return render(request,"app/hotel.html")
def manage(request):
    return render(request,"app/manage.html")
def space(request):
    return render(request,"app/space.html")
def pharm(request):
    return render(request,"app/pharm.html")
def remote(request):
    return render(request,"app/remote.html")


def Administration(request):
    return render(request,"app/Administration.html")

def autodirectory(request):
    return render(request,"app/autodirectory.html")
def busdirectory(request):
    return render(request,"app/busdirectory.html")
def canteens(request):
    return render(request,"app/canteens.html")
def rentals(request):
    return render(request,"app/rentals.html")
def stationary(request):
    return render(request,"app/stationary.html")
def tailor(request):
    return render(request,"app/tailor.html")
