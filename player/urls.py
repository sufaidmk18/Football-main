from django.urls import path
from . import views

urlpatterns = [
    path('phome/',views.phome,name= "phome"),
    path('pdetails/',views.pdetails,name= "pdetails"),
    path('viewp/<int:id>',views.viewp,name= "viewp"),
    path("edit/<int:id>",views.editplayer,name="editplayer"),
    path('pmessages/',views.pmessages,name= "pmessages"),
    path('viewmatch/',views.viewmatch,name= "viewmatch"),
    path('viewperf/',views.viewperf,name= "viewperf"),
    path('viewstat/',views.viewstat,name= "viewstat"),
    path('viewteam/',views.viewteam,name= "viewteam"),

]
