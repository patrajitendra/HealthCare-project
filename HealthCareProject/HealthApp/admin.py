from django.contrib import admin

from .models import DiseaseModel,MedicineModel,UserRegistration


class UserRegistrationModel(admin.ModelAdmin):

    list_display = ['id','firstname','lastname','age','gender','address']
admin.site.register(UserRegistration,UserRegistrationModel)

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['disease_id','disease_name','symptoms',]

admin.site.register(DiseaseModel,DiseaseAdmin)


class MedicineAdmin(admin.ModelAdmin):

    list_display = ['disease_name','symptoms','medicine_name',]

admin.site.register(MedicineModel,MedicineAdmin)







