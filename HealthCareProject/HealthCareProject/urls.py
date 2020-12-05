"""HealthCareProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView,CreateView,View,UpdateView,ListView,DeleteView
from  HealthApp.models import UserRegistration,DiseaseModel,AdminModel,MedicineModel
from django.contrib.messages.views import SuccessMessageMixin
from HealthApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='main'),
    path('register/',CreateView.as_view(model=UserRegistration,fields="__all__" ,template_name="register.html",success_url="/register/",),name='register'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('login/',views.logincheck,name='login'),
    path('adddis/',CreateView.as_view(template_name='Adddisease.html' ,model=DiseaseModel,fields='__all__' ,success_url='/adddis/'),name='adddis'),
    path('viewall/', ListView.as_view(model=DiseaseModel, template_name='ViewDisease.html'), name='viewall'),
    path('modify/<int:pk>',UpdateView.as_view(model=DiseaseModel,fields="__all__",success_url="/viewall/",template_name="update.html"),name='modify'),
    path('delete/<int:pk>',DeleteView.as_view(success_url='/viewall/',model=DiseaseModel,template_name='diseasemodel_confirm_delete.html'),name='delete'),
    path('addmedi/',CreateView.as_view(model=MedicineModel,fields="__all__",success_url="/addmedi/",template_name="AddMedicine.html"),name='addmedi'),
    path('report/',ListView.as_view(model=MedicineModel,template_name='report.html'),name='report'),
    path('viewmedicine/',ListView.as_view(template_name='viewmedicine.html',model=MedicineModel,),name='viewmedicine'),
    path('report_dis/',ListView.as_view(model=MedicineModel,template_name='report_dis.html'),name='report_dis'),
    path('userlogincheck/',TemplateView.as_view(template_name='userlogin.html',),name='userlogincheck'),
    path('loginuser/',views.userlogin,name='loginuser'),
    path('details/',ListView.as_view(template_name='Showdetails.html',model=MedicineModel,),name='details'),
    path('home/',TemplateView.as_view(template_name='welcome.html'),name='home'),
    path('search/', TemplateView.as_view(template_name='medicinesearchuser.html'), name='search'),
    path('searchmedicineuser/',views.searchmedicine),
    path('changepwd/',views.changepassword,name='changepwd'),
    path('savenewpassword/',views.changenewpwd,name='savenewpassword'),



]
