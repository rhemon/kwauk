from django.shortcuts import render

# Create your views here.
def project_list(request):
    return render(request, "shared/projects_list.html", {"projects": Project.objects.all()})

def project_details(request, pid):
    project = Project.objects.get(id=pid)
    if request.method == "POST":
        phone = request.POST.get("phone")
        if User.obejcts.get(username=phone):
            user = User.objects.get(username=phone)
        else:
            user = User.objects.create_user(username=phone, first_name=request.POST.get("first_name"), last_name=request.POST.get("last_name"), password=request.POST.get("phone"))
        ProjectDonations.objects.create(project=project, user=user, amount=request.POST.get("amount"))
    return render(request, "shared/project_details.html", {"project": project})

def user_donations(request):
    donations = ProjectDonations.object.filter(user=request.user)
    return render(request, "member/donations.html", {"donations": donations})