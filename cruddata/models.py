from django.db import models

# Create your models here.

class Crud(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.CharField(max_length=20)  
    econtact = models.CharField(max_length=15)
    efield1 = models.CharField(max_length=15)  
    efield2 = models.CharField(max_length=15)    
    class Meta:  
        db_table = "employee"  