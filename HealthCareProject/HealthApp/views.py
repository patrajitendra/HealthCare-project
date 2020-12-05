from django.shortcuts import render
from HealthApp.models import AdminModel,UserRegistration,MedicineModel
from django.views.generic import View





def adminlogin(request):
    return render(request,'adminlogin.html')


def logincheck(request):
    un=request.POST.get('t1')
    pwd=request.POST.get('t2')
    try:
        AdminModel.objects.get(username=un,password=pwd)
        return render(request,'loginadmin.html')
    except AdminModel.DoesNotExist:
        return render(request,'adminlogin.html',{"error":"Invalid user"})


def userlogin(request):
    un=request.POST.get('t1')
    pwd=request.POST.get('t2')

    try:
        UserRegistration.objects.get(username=un,password=pwd)
        return render(request,'welcome.html')
    except UserRegistration.DoesNotExist:
        return render(request,'userlogin.html',{"error":"Invalid User"})


def searchmedicine(request):
    na = request.POST.get("name")
    mm = MedicineModel.objects.all()
    if mm:
        qs1 = MedicineModel.objects.filter(disease_name=na)
        return render(request, "viewsearch.html", {"res": qs1})
    else:
        return render(request, "medicinesearchuser.html", {"msg": "Data not available"})


def changepassword(request):


    return render(request,'changepassword.html')


def changenewpwd(request):
    oldpassword=request.POST.get('oldpwd')
    newpassword=request.POST.get('newpwd')
    up=UserRegistration.objects.filter(password=oldpassword)

    for x in up:
        if x.password == oldpassword:
            qs=UserRegistration.objects.filter(username= x.username).update(password=newpassword)
            return render(request,'userlogin.html',{"msg":"password has changed","data":qs})
        else:
            return render(request,'changepassword.html',{"error":"Your old password is incorrect"})
    else:
        return render(request, 'changepassword.html', {"error": "Your old password is incorrect"})

