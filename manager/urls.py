from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginn,name= "login"),
    path('Mngrhome',views.Mngrhome,name= "Mngrhome"),
    path('mdetails/',views.mdetails, name = "mdetails"),
    
    path('coaches/',views.coaches, name = "coaches"),
    path('addcoach/',views.addcoach,name=  "addcoach"),
    path('staffs/',views.staffs,name= "staffs"),
    path('addstaff/',views.addstaff,name=  "addstaff"),
    path('viewteam/',views.viewteam,name= "viewteam"),
    
    path('playertable/',views.playertable,name= "playertable"),
    path('viewplayer/<id>',views.viewplayer,name= "viewplayer"),
    path("vpdetails/<int:id>",views.viewpdetails,name="vpdetails"),
    
    path('viewcoach/<int:id>',views.viewcoach,name= "viewcoach"),
    path("edit/",views.editmanager,name="editmanager"),
    path('matches/',views.match,name= "matches"),

]

