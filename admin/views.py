from django.shortcuts import render, redirect
from member.models import *
from django.contrib.auth.models import User

# Create your views here.
def members_list(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect("/http-404")
    users = Member.objects.filter(user__is_active=False)
    active_users = Member.objects.filter(user__is_active=True)
    
    return render(request, "admin/members_list.html", {"photo": Member.objects.get(user=request.user).photo.name, "new_members": users, "active_members": active_users})

def member_detail(request, user_id):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect("/http-404")
    user = User.objects.get(id=user_id)
    member = Member.objects.get(user=user)
    if request.method == "GET":
        return render(request, "admin/member_details.html", {"photo": Member.objects.get(user=request.user).photo.name, "user": user, "member": member})
    else:
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.is_active = request.POST.get("isactive") != None
        member.fathers_name = request.POST.get("fathers_name")
        member.uk_address = request.POST.get("uk_address")
        member.city = request.POST.get("city")
        member.bd_address = request.POST.get("bd_address")
        member.union = request.POST.get("union")
        member.member_type = request.POST.get("member_type")
        password = request.POST.get("password")
        if (password != ""):
            user.set_password(password)
        user.save()
        member.save()
        return redirect("/admin/members")
    
def member_fees(request):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect("/http-404")
    members = Member.objects.filter(member_type="Executive")
    response = []
    for each in members:
        
        mf = {'first_name': each.user.first_name,
        'last_name': each.user.last_name,
        'username': each.user.username,
        'pk': each.id }
        try:
            fee = MemberFee.objects.filter(member=each).latest('paydate')
            mf['paydate'] = fee.paydate
            mf['amount'] = fee.amount
        except:
            mf['paydate'] = 'Not Done Yet'
            mf['amount'] = 0
        response.append(mf)
    return render(request, "admin/member_fees.html", {"photo": Member.objects.get(user=request.user).photo.name, "title": "Member Fees", "exec_members": response})
            
def add_member_pay(request, member_id):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect("/http-404")
    member = Member.objects.get(id=member_id)
    if (request.method == "POST"):
        MemberFee.objects.create(member=member, amount=request.POST.get("amount"), paydate=request.POST.get("paydate"))
        return redirect("/admin/member-fees/")
    else:
        member = member.user
        return render(request, "admin/add_pay.html", {"photo": Member.objects.get(user=request.user).photo.name, "member": member})

def members_all_payments(request, member_id):
    if not (request.user.is_authenticated and request.user.is_superuser):
        return redirect("/http-404")
    if (request.method == "POST"):
        member_fee = MemberFee.objects.get(id=request.POST.get("payid"))
        member_fee.delete()
    member = Member.objects.get(id=member_id)
    member_fees = MemberFee.objects.filter(member=member)
    
    return render(request, "admin/member_all_pay.html", {"photo": Member.objects.get(user=request.user).photo.name, "member": member, "payments": member_fees})
