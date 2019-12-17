from django.shortcuts import render, redirect
from member.models import *
from django.contrib.auth.models import User

# Create your views here.
def members_list(request):
    users = Member.objects.filter(user__is_active=False)

    return render(request, "admin/members_list.html", {"new_members": users})

def member_detail(request, user_id):
    
    user = User.objects.get(id=user_id)
    member = Member.objects.get(user=user)
    if request.method == "GET":
        return render(request, "admin/member_details.html", {"new_user": user, "new_member": member})
    else:
        user.is_active = True
        user.save()
        return redirect("/admin/members")