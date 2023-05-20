from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .form import playerform
from staff.models import *

# Create your views here.
def phome(request):
    context ={}
    if player.objects.filter(login_id=request.session["lid"]).exists():
        context={"id":getplayer(request)}
    else:
        return redirect("pdetails")
    return render(request,'player/phome.html',context)

    
def pdetails(request):
    if request.method=="POST":
        pname=request.POST.get('fname')
        dob=request.POST.get('dob')
        position=request.POST.get('position')
        contact=request.POST.get('contact')
        housename=request.POST.get('hname')
        post=request.POST.get('post')
        place=request.POST.get('place')
        village=request.POST.get('village')
        state=request.POST.get('state')
        district=request.POST.get('district')
        context={"message":"details added"}

        player.objects.create(login_id=request.session["lid"],pname=pname,dob=dob,position=position,contact=contact,housename=housename,post=post,place=place,village=village,district=district,state=state)
        
    return render(request,'player/pdetails.html')
   
    
def getplayer(request):
    return player.objects.get(login_id=request.session["lid"]).id

def viewp(request,id):
    p=player.objects.get(id=id)
    context={"p":p}
    return render(request,'player/viewp.html', context)

def editplayer(request,id):
    context={"form":playerform(instance=player.objects.get(id=id))}
    if request.method=="POST":
        form=playerform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.id=id
            data.save()
            context["message"]="edited"
            return render(request,"form.html",context)
        else:
            context["message"]="something went wrong"
            return render(request,"form.html",context)
    else:
        return render(request,"form.html",context)

def pmessages(request):
    return render(request,'player/pmessages.html')

def viewmatch(request):
    return render(request,'player/viewmatch.html')

def viewperf(request,id):
    p = player.objects.get(id=id)
    context = {"p": p}
    return render(request,'player/viewperf.html',context)

def viewstat(request):
    return render(request,'player/viewstat.html')

def viewteam(request):
    return render(request,'player/viewteam.html')
