from django.db import models
from member.models import *

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextArea()
    target_amount = models.DecimalField(decimal_places=2, max_digits=20)

class ProjectDonations(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    paid = models.BooleanField(default=False)
    paydate = models.DateField(null=True,blank=True)
    commitdate = models.DateField(default_now=True, null=True,blank=True)