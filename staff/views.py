from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .form import staffform,performanceform,Matchform,match_detailsform
from.models import *
from manager.models import login
from django.contrib.auth import login as authlogin, logout , authenticate
from django.http import HttpResponse
from.models import Staff
from django.shortcuts import redirect

# Create your views here.

def stfhome(request):
    context ={}
    if Staff.objects.filter(login_id=request.session["lid"]).exists():
        context={"id":getstaff(request)}
    else:
        return redirect("stfdetails")
    
    return render(request,'staff/stfhome.html',context)

def getstaff(request):
    return Staff.objects.get(login_id=request.session["lid"]).id

def stfdetails(request):
    if request.method=="POST":
        name=request.POST.get('fname')
        dob=request.POST.get('dob')
        contact=request.POST.get('contact')
        housename=request.POST.get('hname')
        post=request.POST.get('post')
        place=request.POST.get('place')
        village=request.POST.get('village')
        state=request.POST.get('state')
        district=request.POST.get('district')
    
        Staff.objects.create(login_id=request.session["lid"],name=name,dob=dob,contact=contact,housename=housename,post=post,place=place,village=village,district=district,state=state)

    return render(request,'staff/stfdetails.html')

def viewstf(request,id):
    stf=Staff.objects.get(id=id)
    context={"stf":stf}
    return render(request,'staff/viewstf.html', context)

def editstaff(request,id):
    context={"form":staffform(instance=Staff.objects.get(id=id))}
    if request.method=="POST":
        form=staffform(request.POST)
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
    
def playerlist(request):
    playerr=player.objects.all()
    context={'playerr':playerr}
    return render(request,'staff/stfplayers.html',context)

def mngplayer(request,id):
    context={"i":id}
    return render(request,'staff/mngplyer.html',context)

def addperfo(request,id):
    context={"name":player.objects.get(id=id).pname}
    pl=player.objects.get(id=id)
    if performance.objects.filter(pname=pl).exists():
        ob=performance.objects.get(pname=pl)
    else:
        ob=performance(pname=pl)
    if request.method=="POST":
        form=performanceform(request.POST,instance=ob)
        if form.is_valid():
            data=form.save(commit=False)
            data.pname_id=id
            data.save()
            return HttpResponse("saved")
        else :
            return HttpResponse("invalid")
    else:
        # if performance.objects.filter(pname=pl).exists():
        #     ob=performance.objects.get(pname=pl)
        # else:
        #     ob=performance(pname=pl)
        context["form"]=performanceform(instance=ob)
        return render(request,"form.html",context)
        # total_matches=request.POST.get('total matchese')
        # goals=request.POST.get('goalscored')
        # assists=request.POST.get('assists')
        # cleansheets=request.POST.get('cleansheets')
        # red_cards=request.POST.get('redcards')
        # yellow_cards=request.POST.get('yellowcard')

        # performance.objects.create(pname=request.session["lid"],total_matches=total_matches,goals=goals,assists=assists,cleansheets=cleansheets,red_cards=red_cards,yellow_cards=yellow_cards)
        

    return render(request,'staff/addperfo.html',context)

def stfcoaches(request):
    coache=Coach.objects.all()
    context={'coache':coache}
    return render(request,'staff/stfcoaches.html',context)

def stfteam(request):
    return render(request,'staff/stfteam.html')

def viewstatistics(request):
    return render(request,'staff/viewstatistics.html')

def viewpdetails(request,id):
    p=player.objects.get(id=id)
    context={"p":p}
    return render(request,'staff/viewpdetails.html',context)

def viewstatistics(request):
    return render(request,'staff/viewstatistics.html')

def stfmatches(request):
    return render(request,'staff/stfmatches.html')

def newmatch(request):
    context={}
    if request.method == "POST":
        form = Matchform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else :
            return HttpResponse("inavlid")
    else:
        context["form"]=Matchform()
        return render(request,'form.html',context)
from datetime import date, timedelta
def upcoming(request):
    a={"data":Match.objects.all().filter(date__gte=date.today()).order_by('date')}
    return render(request,'staff/upcoming.html',a)



def played(request):
    context={"data":match_details.objects.all()}
    return render(request,'staff/played.html',context)

def editmatchdetails(request,id):
 
    return render(request,'staff/editmatchdetails.html')

def addmatchdetails(request,id):
    context={}
    if request.method == "POST":
        form = match_detailsform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.Match_id=id
            if match_details.objects.filter(id=id).exists():
                ob=match_details.objects.get(id=id)
                data.id=ob.id
            data.save()

            return HttpResponse("saved")
        else :
            return HttpResponse("inavlid")
    else:
        if match_details.objects.filter(Match_id=id).exists():
            matchobject=match_details.objects.get(Match_id=id)
        else:
            matchobject=match_details(Match_id=id)
        context["form"]=match_detailsform(instance=matchobject)
        return render(request,'form.html',context)