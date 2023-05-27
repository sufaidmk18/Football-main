from .models import track_statistics
from .models import team, team_type
from datetime import date, timedelta
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


def comingm(request):
    a = {"data": Match.objects.all().filter(
        date__gte=date.today()).order_by('date')}
    return render(request, 'coach/comingm.html', a)


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
        date_ob = f"{datetime.today().year}-{datetime.today().month}-{datetime.today().day}"
        model_statictics.objects.create(pname_id=pid)
        track_statistics.objects.create(player_id=pid, date=date_ob)
        return render(request, "original/coach/statistics.html", {"data": model_statictics.objects.get(pname_id=pid)})


def editstatic(request, atri, add_sub, player_id):
    date_ob = f"{datetime.today().year}-{datetime.today().month}-{datetime.today().day}"
    if track_statistics.objects.filter(player_id=player_id, date=date_ob).exists():
        track_statistics_ob = track_statistics.objects.get(
            date=date_ob, player_id=player_id)
    else:
        track_statistics_ob = track_statistics.objects.create(
            player_id=player_id, date=date_ob)
        print(False)
    print(date_ob)
    statistics_object = model_statictics.objects.get(pname_id=player_id)
    if atri == "bollcontronl":
        if add_sub == 0 and statistics_object.bollcontronl-1 >= 0:
            statistics_object.bollcontronl = statistics_object.bollcontronl - 1
            track_statistics_ob.bollcontronl = statistics_object.bollcontronl
        elif add_sub == 1 and statistics_object.bollcontronl+1 <= 100:
            statistics_object.bollcontronl = statistics_object.bollcontronl + 1
            track_statistics_ob.bollcontronl = statistics_object.bollcontronl
    elif atri == "passaccuracy":
        if add_sub == 0 and statistics_object.passaccuracy-1 >= 0:
            statistics_object.passaccuracy = statistics_object.passaccuracy - 1
            track_statistics_ob.passaccuracy = statistics_object.passaccuracy
        elif add_sub == 1 and statistics_object.passaccuracy+1 <= 100:
            statistics_object.passaccuracy = statistics_object.passaccuracy + 1
            track_statistics_ob.passaccuracy = statistics_object.passaccuracy
    elif atri == "stamina":
        if add_sub == 0 and statistics_object.stamina-1 >= 0:
            statistics_object.stamina = statistics_object.stamina - 1
        elif add_sub == 1 and statistics_object.stamina+1 <= 100:
            statistics_object.stamina = statistics_object.stamina + 1
        track_statistics_ob.stamina = statistics_object.stamina
    elif atri == "speed":
        if add_sub == 0 and statistics_object.speed-1 >= 0:
            statistics_object.speed = statistics_object.speed - 1
            track_statistics_ob.speed = statistics_object.speed
        elif add_sub == 1 and statistics_object.speed+1 <= 100:
            statistics_object.speed = statistics_object.speed + 1
            track_statistics_ob.speed = statistics_object.speed
    elif atri == "takles":
        if add_sub == 0 and statistics_object.takles-1 >= 0:
            statistics_object.takles = statistics_object.takles - 1
            track_statistics_ob.takles = track_statistics_ob.takles
        elif add_sub == 1 and statistics_object.takles+1 <= 100:
            statistics_object.takles = statistics_object.takles + 1
            track_statistics_ob.takles = track_statistics_ob.takles
    elif atri == "shoot":
        if add_sub == 0 and statistics_object.shoot-1 >= 0:
            statistics_object.shoot = statistics_object.shoot - 1
            track_statistics_ob.shoot = statistics_object.shoot
        elif add_sub == 1 and statistics_object.shoot+1 <= 100:
            statistics_object.shoot = statistics_object.shoot + 1
            track_statistics_ob.shoot = statistics_object.shoot

    track_statistics_ob.save()
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
    sta = model_statictics.objects.get(pname=p)
    data = [sta.bollcontronl, sta.passaccuracy,
            sta.stamina, sta.speed, sta.takles, sta.shoot]
    context = {"p": p, "data": data}
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


def total_statictics(request):
    bollcontrol_database = model_statictics.objects.all()
    names = []
    bollcontrol = []
    passaccuracy = []
    stamina = []
    takles = []
    shoot = []

    for i in bollcontrol_database:
        names.append(i.pname.pname)
        bollcontrol.append(i.bollcontronl)
        passaccuracy.append(i.passaccuracy)
        stamina.append(i.stamina)
        takles.append(i.takles)
        shoot.append(i.shoot)

        # daily  track database
    daily_track_data = track_statistics.objects.all()
    players_list = []
    for i in daily_track_data:
        if (i.player in players_list):
            continue
        else:
            players_list.append(i.player)
    daily_context_data = []

    for i in players_list:
        single_player_ob = track_statistics.objects.all().filter(player=i)
        single_ob = {"id": i.id, "name": i.pname, "date": [], "bollcontronl": [], "passaccuracy": [
        ], "stamina": [], "speed": [], "takles": [], "shoot": []}
        for i in single_player_ob:
            single_ob["date"].append(i.date)
            single_ob["bollcontronl"].append(i.bollcontronl)
            single_ob["passaccuracy"].append(i.passaccuracy)
            single_ob["stamina"].append(i.stamina)
            single_ob["speed"].append(i.speed)
            single_ob["takles"].append(i.takles)
            single_ob["shoot"].append(i.shoot)
        daily_context_data.append(single_ob)
    print(daily_context_data)
    context = {"name": names, "bollcontrol": bollcontrol, "passaccuracy": passaccuracy,
               "stamina": stamina, "takles": takles, "shoot": shoot, "daily": daily_context_data}
    return render(request, "coach/total_statictics.html", context)


def team_view(request):
    team_ob_tens = team.objects.all().filter(type_id=1)
    team_ob_sevens = team.objects.all().filter(type_id=2)
    team_ob_fives = team.objects.all().filter(type_id=3)
    context = {"team_tens": team_ob_tens,
               "team_fives": team_ob_fives, "team_sevens": team_ob_sevens}
    return render(request, "coach/team.html", context)


def addtoteam(request, player_id, team_id):
    if team.objects.filter(pname_id=player_id).exists():
        team_ob = team.objects.get(pname_id=player_id)
        team_ob.type_id = team_id
        team_ob.save()
    else:
        team.objects.create(pname_id=player_id, type_id=team_id)
    return redirect("viewteams")


def removefromteam(request, player_id):
    team.objects.get(pname_id=player_id).delete()
    return redirect("viewteams")
