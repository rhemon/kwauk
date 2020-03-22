from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.
def search_help_post(request):
    posts = HelpPost.objects.filter(resolved=False).order_by("area")
    if request.method=="POST":
        search_key = request.POST.get("search")
        posts = HelpPost.objects.filter(Q(postcode__startswith=search_key) | Q(phone=search_key) | Q(area__iexact=search_key))
        posts = posts.filter(resolved=False)
    return render(request, "coronahelp/index.html", {"posts": posts})

def new_help_post(request):
    if (request.method=="GET"):
        return render(request, "coronahelp/new.html", {})
    else:
        HelpPost.objects.create(description=request.POST.get("description"), postcode=request.POST.get("postcode"), area=request.POST.get("area"), phone=request.POST.get("phone"), name=request.POST.get("name"), secret_key=request.POST.get("secret_key"))
        return redirect("/coronahelp/")

def resolve_help_post(request, pid):
    post_id = pid
    help_post = HelpPost.objects.get(id=post_id)
    if (request.method=="GET"):
        return render(request, "coronahelp/resolve.html", {"post": help_post, "emsg": ""})
    if (help_post.secret_key == request.POST.get("secret_key")):
        help_post.resolved = True
        help_post.save()
        return redirect("/coronahelp/")
    else:
        return render(request, "coronahelp/resolve.html", {"post":help_post, "emsg":"Problem can be resolved by the person seeking help with his set password. If you are the helper, contact the help seeker with given details."})
