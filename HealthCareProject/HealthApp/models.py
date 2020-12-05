from django.db import models



class UserRegistration(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.TextField()
    username=models.CharField(unique=True,max_length=10)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname

class AdminModel(models.Model):
    username=models.CharField(unique=True,max_length=200)
    password=models.CharField(max_length=50)

class DiseaseModel(models.Model):
    disease_id=models.AutoField(primary_key=True)
    disease_name=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=200,default=False)

class MedicineModel(models.Model):
    disease_name=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=200)
    medicine_name=models.CharField(max_length=200)
    medicine_description=models.TextField()
    name=models.ManyToManyField(DiseaseModel)
