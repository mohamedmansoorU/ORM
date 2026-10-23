# Ex02 Django ORM Web Application
## Date: 07.10.26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import customer_DB,customer_DBAdmin
admin.site.register(customer_DB,customer_DBAdmin)

models.py
from django.db import models
from django.contrib import admin
class customer_DB(models.Model):
    Name=models.CharField(max_length=20)
    phone_num=models.IntegerField()
    vechile_number=models.CharField(max_length=20)
    vechicle_model=models.CharField(max_length=20)
    service_mode=models.CharField(max_length=20)
    bill_no=models.IntegerField()
    email=models.CharField(max_length=30)
class customer_DBAdmin(admin.ModelAdmin):
    list_display=["Name","phone_num","vechile_number","vechicle_model","service_mode","bill_no","email"]
```

## OUTPUT
![alt text](<Screenshot (8).png>)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
