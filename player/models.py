from django.db import models
# Create your models here.

def get_default_value():
    return "enter"

class playerauth(models.Model):
    name=models.CharField( max_length=50)
    password=models.IntegerField()
from manager.models import login

class player(models.Model):
    login=models.ForeignKey(login, on_delete=models.CASCADE,null=True)
    pname=models.CharField( max_length=50,null=True)
    dob=models.DateField( auto_now=False, auto_now_add=False,null=True)
    contact=models.IntegerField(null=True)
    def __str__(self) :
        return self.pname
    # photo=models.FileField(upload_to=None, max_length=100)
    posi=[
    ("Centre-back", "Centre-back"),
    ("Full-back", "Full-back"),
    ('left wing back', 'left wing back'),
    ('right wing back', 'right wing back'),
    ("Central midfielder", "Central midfielder"),
    ("Defensive midfielder", "Defensive midfielder"),
    ("Attacking midfielder", "Attacking midfielder"),
    ("Centre forward", "Centre forward"),
    ('left forward', 'left forward'),
    ('right forward', 'right forward'),
    ("Goalkeeper", "Goalkeeper")
    ]
    position=models.CharField(null=True, max_length=50)
    post=models.CharField( max_length=50,null=True)
    housename=models.CharField(max_length=50,null=True)
    place=models.CharField(max_length=50,null=True)
    village=models.CharField(default=get_default_value,max_length=50,null=True)
    district=models.CharField( max_length=50,null=True)
    state=models.CharField(default=get_default_value,max_length=50,null=True)
    coach=models.IntegerField(default=0)


