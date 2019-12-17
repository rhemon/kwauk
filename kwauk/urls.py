"""kwauk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admin import views as admin
from member import views as member
from .views import *

urlpatterns = [
    path('', index),
    path('register/', member.register),
    path('registered/', member.registered),
    path('member/', member.dashboard),
    path('login/', member.login),
    path('logout/', member.logout),
    path('admin/members', admin.members_list),
    path('admin/member/<user_id>/', admin.member_detail),
    path('member/not-activated/', member.notactivated)
]
