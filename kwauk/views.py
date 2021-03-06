from django.shortcuts import HttpResponse, render
from django.contrib.auth.models import User
from member.models import *
def index(request):
    users = Member.objects.filter(user__is_active=True)
    return render(request, "shared/home.html", {"users": users})

def http404(request):
    return HttpResponse("HTTP 404 - Page Not Found")