from coach.models import team
from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from coach.models import Coach
from staff.models import Staff
from .form import Managerform
from player.models import player
from staff.models import Match

# Create your views here.


def loginn(request):
    msg = ""
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['psw']
        res = login.objects.filter(username=username, password=password)
        if res.exists():
            d = login.objects.get(username=username, password=password)
            request.session["lid"] = d.id
            if d.usertype == "manager":
                return redirect('Mngrhome')
            elif d.usertype == "coach":
                a = login.objects.get(
                    username=username, password=password, usertype="coach")
                request.session["id"] = a.id
                return redirect('Chome')
            elif d.usertype == "player":
                return redirect('phome')
            elif d.usertype == "staff":
                return redirect('stfhome')

            else:
                msg = "your not a user in this academy"

    return render(request, 'original/login.html', {'msg': msg})


def samplelogin(request):
    return render(request, "original/index.html")


def coach(request):
    if request.method == 'POST':
        return render(request, 'manager/playertable.html')
    else:

        return render(request, 'manager/coach.html')


def mdetails(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')
        housename = request.POST.get('hname')
        post = request.POST.get('post')
        place = request.POST.get('place')
        village = request.POST.get('village')
        state = request.POST.get('state')
        district = request.POST.get('district')

        manager.objects.create(login_id=request.session["lid"], name=name, dob=dob, contact=contact,
                               housename=housename, post=post, place=place, village=village, district=district, state=state)

    return render(request, 'manager/mdetails.html')


def getmanager(request):
    return manager.objects.get(login_id=request.session["lid"])


def coaches(request):
    context = {"coach": Coach.objects.all()}
    print(Coach.objects.all())
    return render(request, 'original/manager/coach.html', context)


def staffs(request):
    context = {"staff": Staff.objects.all()}
    print(Staff.objects.all())
    return render(request, 'original/manager/staff.html', context)


def addcoach(request):
    if request.method == "POST":
        username = request.POST.get('fname',)
        password = request.POST.get('password')

        data = login(username=username, password=password,
                     usertype='coach').save()

        return HttpResponse('<script>alert("new coach added");window.location=""</script>')
    else:
        return render(request, 'manager/addcoach.html')


def viewteams(request):
    team_object = team.objects.all()
    return render(request, 'original/manager/team.html', {"team": team_object})


def addtoteam(request, id):
    player_object = player.objects.get(id=id)
    if team.objects.filter(pname_id=player_object.id):
        return redirect("viewteams")
    else:
        team.objects.create(pname=player_object)
        return redirect("viewteams")


def playertable(request):
    playerr = player.objects.all()
    context = {'playerr': playerr}
    return render(request, 'original/manager/player.html', context)


def viewplayer(request, id):
    context = {"i": id}
    return render(request, 'manager/viewplayer.html', context)


def viewpdetails(request, id):
    p = player.objects.get(id=id)
    context = {"p": p}
    return render(request, 'manager/viewpdetails.html', context)


def addstaff(request):
    if request.method == "POST":
        username = request.POST.get('fname',)
        password = request.POST.get('password')

        data = login(username=username, password=password,
                     usertype='staff').save()

        return HttpResponse('<script>alert("new staff added");window.location=""</script>')
    else:
        return render(request, 'manager/addstaff.html')


def Mngrhome(request):
    return render(request, 'original/manager/main.html')


def viewcoach(request, id):
    co = Coach.objects.get(id=id)
    context = {"co": co}
    return render(request, 'manager/viewcoach.html', context)


def viewm(request):
    m = manager.objects.get()
    context = {"m": m}
    return render(request, 'manager/viewm.html', context)


def editmanager(request):
    context = {"form": Managerform(instance=manager.objects.get())}
    if request.method == "POST":
        form = Managerform(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.id = id
            data.save()
            context["message"] = "edited"
            return render(request, "form.html", context)
        else:
            context["message"] = "something went wrong"
            return render(request, "form.html", context)
    else:
        return render(request, "form.html", context)


def match(request):
    return render(request, 'manager/matches.html')


def upcoming(request):
    a = {"data": Match.objects.all().filter(
        date__gte=date.today()).order_by('date')}
    return render(request, 'staff/upcoming.html', a)
