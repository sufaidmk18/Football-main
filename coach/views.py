from .models import statistics as model_statictics
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from manager.models import login
from player.models import player
from staff.models import Match
from .form import Coachform
from .models import player, attendance
from django.shortcuts import redirect
from django.contrib.auth import login as authlogin, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# def reigster(request):
#     context={}
#     if request.method == "POST":
#         coachform=Coachform(request.POST)
#         userform=UserCreationForm(request.POST)
#         if userform.is_valid() and coachform.is_valid():
#             data=coachform.save()
#             userob=userform.save(commit=False)
#             userob.username="co"+str(data.id)
#             userob.save()
#             return HttpResponse("couach added")
#         else:
#             return HttpResponse("please enter all data")
#     else:
#         return HttpResponse("form")


def Chome(request):
    context = {}
    if Coach.objects.filter(login_id=request.session["lid"]).exists():
        context = {"id": getcoach(request)}
    else:
        return redirect("Cdetails")

    return render(request, 'original/coach/main.html', context)


def players(request):
    return render(request, 'coach/players.html')


def playerlist(request):
    playerr = player.objects.all().filter(coach=getcoach(request))
    context = {'playerr': playerr}
    return render(request, 'original/coach/player.html', context)

from datetime import date, timedelta
def comingm(request):
    a={"data":Match.objects.all().filter(date__gte=date.today()).order_by('date')}
    return render(request,'coach/comingm.html',a)


def addplayer(request):
    if request.method == "POST":
        username = request.POST.get('fname',)
        password = request.POST.get('password')

        data = login(username=username, password=password,
                     usertype='player').save()

        player(pname=username, coach=getcoach(request)).save()
        return HttpResponse('<script>alert("new player added");window.location=""</script>')

    else:
        return render(request, 'coach/addplayer.html')


def Statistics(request, pid):
    if model_statictics.objects.filter(pname_id=pid).exists():
        return render(request, "original/coach/statistics.html", {"data": model_statictics.objects.get(pname_id=pid)})
    else:
        model_statictics.objects.create(pname_id=pid)
        return render(request, "original/coach/statistics.html", {"data": model_statictics.objects.get(pname_id=pid)})


def editstatic(request, atri, add_sub, player_id):
    statistics_object = model_statictics.objects.get(pname_id=player_id)
    if atri == "bollcontronl":
        if add_sub == 0 and statistics_object.bollcontronl-1 >= 0:
            statistics_object.bollcontronl = statistics_object.bollcontronl - 1
        elif add_sub == 1 and statistics_object.bollcontronl+1 <= 100:
            statistics_object.bollcontronl = statistics_object.bollcontronl + 1
    elif atri == "passaccuracy":
        if add_sub == 0 and statistics_object.passaccuracy-1 >= 0:
            statistics_object.passaccuracy = statistics_object.passaccuracy - 1
        elif add_sub == 1 and statistics_object.passaccuracy+1 <= 100:
            statistics_object.passaccuracy = statistics_object.passaccuracy + 1
    elif atri == "stamina":
        if add_sub == 0 and statistics_object.stamina-1 >= 0:
            statistics_object.stamina = statistics_object.stamina - 1
        elif add_sub == 1 and statistics_object.stamina+1 <= 100:
            statistics_object.stamina = statistics_object.stamina + 1
    elif atri == "speed":
        if add_sub == 0 and statistics_object.speed-1 >= 0:
            statistics_object.speed = statistics_object.speed - 1
        elif add_sub == 1 and statistics_object.speed+1 <= 100:
            statistics_object.speed = statistics_object.speed + 1
    elif atri == "takles":
        if add_sub == 0 and statistics_object.takles-1 >= 0:
            statistics_object.takles = statistics_object.takles - 1
        elif add_sub == 1 and statistics_object.takles+1 <= 100:
            statistics_object.takles = statistics_object.takles + 1
    elif atri == "shoot":
        if add_sub == 0 and statistics_object.shoot-1 >= 0:
            statistics_object.shoot = statistics_object.shoot - 1
        elif add_sub == 1 and statistics_object.shoot+1 <= 100:
            statistics_object.shoot = statistics_object.shoot + 1

    statistics_object.save()
    return redirect("statistics", pid=player_id)


def Attendance(request):
    return render(request, 'coach/attendance.html')


def Cdetails(request):
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

        Coach.objects.create(login_id=request.session["lid"], name=name, dob=dob, contact=contact,
                             housename=housename, post=post, place=place, village=village, district=district, state=state)

    return render(request, 'coach/Cdetails.html')


def getcoach(request):
    return Coach.objects.get(login_id=request.session["lid"]).id


def today(request):
    players = player.objects.all().filter(coach=getcoach(request))
    context = {"data": players}
    attendance_data = []
    date = request.GET.get('date', False)
    if not date:
        month = str(datetime.utcnow().date().month)
        if len(month) == 1:
            month = "0"+month
        date = str(datetime.utcnow().date().year)+"-" + \
            month+"-"+str(datetime.utcnow().date().day)
    print(date)
    for i in players:
        values = {}
        values["id"] = i.id
        values["player_name"] = i.pname

        if attendance.objects.filter(date=date, pname=i).exists():
            values["attendance_present"] = True
            values["attendance_absent"] = False
        else:
            values["attendance_present"] = False
            values["attendance_absent"] = True
        attendance_data.append(values)
    print(date)

    context["date"] = date
    context["attendance_data"] = attendance_data
    return render(request, 'coach/today.html', context)

# def add_attendance(request,playerid,date,status):
#     attendance.objects.create(pname_id=playerid,status=status,date=date)
#     return HttpResponse("updated")


def add_attendence(request, player_id, val, date):
    if attendance.objects.filter(pname_id=player_id, date=date).exists():
        a = attendance.objects.get(pname_id=player_id, date=date)
        a.status = val
        a.save()
        return HttpResponse("changed")
    else:
        attendance.objects.create(pname_id=player_id, date=date, status=val)
        return HttpResponse("created")


def get_attendance(request, playerid, date):
    return HttpResponse("get data")


def stdhome(request, id):
    context = {"i": id}
    return render(request, 'coach/stdhome.html', context)


def viewSdetails(request, id):
    p = player.objects.get(id=id)
    context = {"p": p}
    return render(request, 'coach/viewSdetails.html', context)


def viewc(request, id):
    co = Coach.objects.get(id=id)
    context = {"co": co}
    return render(request, 'coach/viewc.html', context)


def editcoach(request, id):
    context = {"form": Coachform(instance=Coach.objects.get(id=id))}
    if request.method == "POST":
        form = Coachform(request.POST)
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
    return render(request, 'coach/match.html')
