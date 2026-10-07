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
