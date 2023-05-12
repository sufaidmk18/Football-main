from django.contrib.auth.models import User
from django.db import models
from player.models import player
from manager.models import login
# Create your models here.


def get_default_value():
    return "0"


class Coach(models.Model):
    login = models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    # photo=models.FileField(upload_to=None, max_length=100)
    contact = models.IntegerField(default=get_default_value, null=True)
    housename = models.CharField(max_length=50, null=True)
    post = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)


class team(models.Model):
    pname = models.ForeignKey(player, on_delete=models.CASCADE)
    # match=models.ForeignKey(Match, on_delete=models.CASCADE)


class statistics(models.Model):
    pname = models.ForeignKey(player, on_delete=models.CASCADE)
    bollcontronl = models.IntegerField(default=50)
    passaccuracy = models.IntegerField(default=50)
    stamina = models.IntegerField(default=50)
    speed = models.IntegerField(default=50)
    takles = models.IntegerField(default=50)
    shoot = models.IntegerField(default=50)


class attendance(models.Model):
    pname = models.ForeignKey(player, on_delete=models.CASCADE)
    status = models.BooleanField()
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)


class coachauth(models.Model):
    name = models.CharField(max_length=50)
    password = models.IntegerField()
