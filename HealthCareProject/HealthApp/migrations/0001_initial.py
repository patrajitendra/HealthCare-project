# Generated by Django 3.1.2 on 2020-11-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseModel',
            fields=[
                ('disease_id', models.AutoField(primary_key=True, serialize=False)),
                ('disease_name', models.CharField(max_length=200)),
                ('symptoms', models.CharField(default=False, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=200)),
                ('medicine_name', models.CharField(max_length=200)),
                ('medicine_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]