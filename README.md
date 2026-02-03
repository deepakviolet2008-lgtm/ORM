# Ex02 Django ORM Web Application
## Date: 30/01/2026

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class foodappDB(models.Model):
	order_id=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=20)
	Food_Amount=models.FloatField()
	delivery_charge=models.FloatField()
	Food_name=models.CharField(max_length=30)
	Address=models.CharField(max_length=100)
	order_date=models.DateField()
	order_time=models.TimeField()
	Mobile_no=models.IntegerField()
class foodappDBAdmin(admin.ModelAdmin):
	list_display=['order_id','Name','Food_Amount','delivery_charge','Food_name','Address','order_date','order_time','Mobile_no'];

admin.py
from django.contrib import admin
from .models import foodappDB,foodappDBAdmin
admin.site.register(foodappDB,foodappDBAdmin)

```

## OUTPUT
![alt text](<Screenshot 2026-01-30 144445.png>)



## RESULT
Thus the program for creating online food delivery website database using ORM hass been executed successfully
