from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50,null=False)
    loc=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    Firstname=models.CharField(max_length=50,null=False)
    Lastname=models.CharField(max_length=50,default='N/A')
    dept=models.ForeignKey("Department", on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey("Role", on_delete=models.CASCADE)
    hiredate=models.DateField()
    def __str__(self):
        return self.Firstname
