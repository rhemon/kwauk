from django.shortcuts import render, redirect, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login_user,
from .models import *

def login(request):
    if (request.method == "GET"):
        return render(request, "login.html", {})
    else:
        user = authenticate(request, username=request.POST.get("phone"), password=request.POST.get("password"))
        if (user is not None):
            if (user.is_active):
                return redirect("/member/not-activated/")
            login(request, user)
            return redirect("/member")
        else:
            return render(request, "login.html", {"error": "User details entered incorrectly."})

def logout(request):
    logout(request)
    return redirect("/")
        
# Create your views here.
def register(request):
    if (request.method == "GET"):
        return render(request, "member/register.html", {})
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=phone)
            if user.is_active:
                return "Member account already exists"
            user.email = email
            user.password = password
            user.save()
        except:
            user = User.objects.create_user(first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    username=phone,
                                    password=password,
                                    is_active=False)

        member = Member.objects.create(
            user=user,
            fathers_name=request.POST.get("fathers_name"),
            uk_address=request.POST.get("uk_address")
            city=request.POSt.get("city")
            bd_address=request.POST.get("bd_address"),
            union=request.POST.get("union")
            member_type=request.POST.get("member_type")
        )

        return redirect("/registered/")

def registered(request):
    return render(request, "member/registered.html", {})

def dashboard(request):
    return render(request, "member/meber_details.html", {})
