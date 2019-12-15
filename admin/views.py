from django.shortcuts import render
from member.models import *
from django.contrib.auth.models import User

# Create your views here.
def members_list(request):
    users = Member.objects.filter(user__is_active=False)
    return render()

def member_detail(request, user_id):
    pass
