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
