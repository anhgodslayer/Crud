from django.db import models

# Create your models here.

class Crud(models.Model):  
    id = models.CharField(primary_key = True ,max_length=20)  
    title = models.CharField(max_length=100)  
    link = models.CharField(max_length=20)  
    published = models.CharField(max_length=15)   
    class Meta:  
        db_table = "web"  