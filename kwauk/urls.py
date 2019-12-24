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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
    path('http-404/', http404),
    path('register/', member.register),
    path('registered/', member.registered),
    path('member/', member.dashboard),
    path('login/', member.login),
    path('logout/', member.logout),
    path('admin/members/', admin.members_list),
    path('admin/member-fees/', admin.member_fees),
    path('admin/add-pay/<member_id>', admin.add_member_pay),
    path('admin/member/fees/<member_id>', admin.members_all_payments),
    path('admin/member/<user_id>/', admin.member_detail),
    path('member/not-activated/', member.notactivated)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)