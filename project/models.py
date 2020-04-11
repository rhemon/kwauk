from django.db import models
from member.models import *
import datetime
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_amount = models.DecimalField(decimal_places=2, max_digits=20)
    hide = models.BooleanField(default=False)
    

class ProjectDonations(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    paid = models.BooleanField(default=False)
    paydate = models.DateField(null=True,blank=True)
    commitdate = models.DateField(default=datetime.date.today, null=True,blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)

class Distributions(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    fathers_name = models.CharField(max_length=200, null=True, blank=True)
    union = models.CharField(max_length=200, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
