from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your views here.
def project_list(request):
    projects = []
    for each in Project.objects.filter(hide=False):
        p = {}
        p['name'] = each.name
        p['slug'] = each.name.replace(' ', '-')
        p['id'] = each.id
        p['target_amount'] = each.target_amount
        projects.append(p)
    return render(request, "shared/projects_list.html", {"projects": projects})

def project_details(request, pid, name):
    project = Project.objects.get(id=pid)
    msg = ""
    if request.method == "POST":
        phone = request.POST.get("phone")
        try:
            user = User.objects.get(username=phone)
        except:
            user = User.objects.create_user(username=phone, first_name=request.POST.get("first_name"), last_name=request.POST.get("last_name"), password=request.POST.get("phone"), is_active=False)
        ProjectDonations.objects.create(project=project, user=user, amount=request.POST.get("amount"))
        
        
        msg = "Donated £" + str(request.POST.get("amount")) + " successfully!" 
    donations = []
    for each in ProjectDonations.objects.all():
        donation = {}
        donation['name'] = each.user.first_name + " " + each.user.last_name
        donation['paid'] = each.paid
        try:
            donation['img'] = Member.objects.get(user=each.user).photo.name
        except:
            donation['img'] = 'default.jpg'
        donations.append(donation)
    donations = sorted(donations key=lambda x: x['name'])
    total = ProjectDonations.objects.all().aggregate(sum=Sum('amount'))['sum']
    return render(request, "shared/project_details.html", {"project": project, "msg":msg, 'total': total, 'donations': donations})

def user_donations(request):
    donations = ProjectDonations.objects.filter(user=request.user)
    return render(request, "member/donations.html", {"photo": Member.objects.get(user=request.user).photo.name,"donations": donations})