from django.db import models

# Create your models here.

class Employees(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    age=models.PositiveIntegerField()
    contact=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    

