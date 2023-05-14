
from django.urls import path
from . import views

urlpatterns = [
    path('Chome/', views.Chome, name="Chome"),
    path('viewc/<int:id>', views.viewc, name="viewc"),
    path("edit/<int:id>", views.editcoach, name="editcoach"),
    path('Cdetails/', views.Cdetails, name="Cdetails"),
    path('players/', views.players, name="players"),
    path('player/', views.playerlist, name="player"),
    path('addplayer/', views.addplayer, name="addplayer"),
    path('attendance/', views.Attendance, name="attendance"),
    path('add/attendance/<int:player_id>/<int:val>/<str:date>',
         views.add_attendence, name="add_attendence"),
    path('statistics/<int:pid>', views.Statistics, name="statistics"),
    path('editstatic/<str:atri>/<int:add_sub>/<player_id>',
         views.editstatic, name="editstatic"),
    path('today/', views.today, name="today"),

    path('stdhome/<id>', views.stdhome, name="stdhome"),
    path('viewSdetails/<int:id>', views.viewSdetails, name="viewSdetails"),

    path('match/', views.match, name="match"),
    path('comingm/', views.comingm, name="comingm"),
    path('static/', views.total_statictics, name="total_statictics"),

]
