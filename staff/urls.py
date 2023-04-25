from django.urls import path
from . import views

urlpatterns = [
    path('staffhome/',views.stfhome,name= "stfhome"),
    path('staffdetails/',views.stfdetails,name= "stfdetails"),
    path("edit/<int:id>",views.editstaff,name= "editstaff"),
    path("viewstf/<int:id>",views.viewstf,name= "viewstf"),

    path('players/',views.playerlist,name= "stfplayer"),
    path('manageplayer/<id>',views.mngplayer,name= "mngplayer"),
    path('addperformance/<int:id>',views.addperfo,name= "addperfo"),
    path('pdetails/<int:id>',views.viewpdetails,name= "viewpdetails"),
    path('stfstatistics/<int:id>',views.viewstatistics,name= "viewstatistics"),

    path('stfcoaches/',views.stfcoaches,name= "stfcoaches"),
     
    path('stfteam/',views.stfteam,name= "stfteam"),
    
    path('stfmatches/',views.stfmatches,name= "stfmatches"),
    path('newmatch/',views.newmatch,name= "newmatch"),
    path('upcoming/',views.upcoming,name= "upcoming"),
    path('played/',views.played,name= "played"),
    path('editmatchdetails/<int:id>',views.editmatchdetails,name= "editmatchdetails"),
    path('addmatchdetails/<int:id>',views.addmatchdetails,name= "addmatchdetails"),


]

