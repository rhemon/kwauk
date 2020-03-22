from django.db import models
from member.models import *

# Create your models here.
class HelpPost(models.Model):
    description = models.TextField()
    postcode = models.CharField(max_length=10)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    resolved = models.BooleanField(default=False)