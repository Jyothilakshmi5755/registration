from django.db import models
from django.contrib.auth.models import AbstractUser



#Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField()
    phone=models.CharField(max_length=10)


class employee(models.Model):
    Emp_id=models.IntegerField()
    Emp_name=models.CharField(max_length=50)
    place=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    salary=models.IntegerField()