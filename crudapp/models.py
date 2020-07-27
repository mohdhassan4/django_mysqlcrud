from django.db import models

# Create your models here.
class employee(models.Model):
     eid=models.CharField(max_length=20)
     ename=models.CharField(max_length=40)
     eemail=models.EmailField()
     econtact=models.CharField(max_length=15)
     class meta:
         db_table="Employee"  # class name and db_table name inside meta should not same
         