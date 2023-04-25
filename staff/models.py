from django.db import models
from player.models import player
from coach.models import *

# Create your models here.
def get_default_value():
    return "0"

class Staff(models.Model):
    login=models.ForeignKey(login, on_delete=models.CASCADE,null=True)
    name=models.CharField( max_length=50,null =True)
    dob=models.DateField( auto_now=False, auto_now_add=False,null =True)
    # photo=models.FileField(upload_to=None, max_length=100)
    contact=models.IntegerField(default=get_default_value,null =True)
    housename=models.CharField(max_length=50,null =True)
    post=models.CharField( max_length=50,null =True)
    place=models.CharField(max_length=50,null =True)
    village=models.CharField(max_length=50,null =True)
    district=models.CharField( max_length=50,null =True)
    state=models.CharField(max_length=50,null =True)


class performance(models.Model):
    pname=models.ForeignKey(player, on_delete=models.CASCADE)
    total_matches=models.IntegerField()
    goals=models.IntegerField()
    assists=models.IntegerField()
    cleansheets=models.IntegerField()
    red_cards=models.IntegerField()
    yellow_cards=models.IntegerField()


    

class staffauth(models.Model):
    name=models.CharField( max_length=50)
    password=models.IntegerField()

class Match(models.Model):
    opposite_team=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    date=models.DateField( auto_now=False, auto_now_add=False)
    time=models.TimeField( auto_now=False, auto_now_add=False)
    def __str__(self) :
        return self.opposite_team
choiceopt=[
    ("win","win"),
    ("loss","loss"),
    ("draw","draw")
]
class match_details(models.Model):
    Match=models.ForeignKey(Match, on_delete=models.CASCADE)
    status=models.CharField(choices=choiceopt,max_length=50)
    goal_scored=models.IntegerField()
    goal_owned=models.IntegerField()