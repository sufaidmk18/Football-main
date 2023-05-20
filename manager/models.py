from django.db import models

# Create your models here.
def get_default_value():
    return "0"

class login(models.Model):
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    usertype=models.CharField(max_length=52)

class manager(models.Model):
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


    

