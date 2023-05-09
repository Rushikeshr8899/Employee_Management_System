from django.db import models as m

# Create your models here.
class Roles(m.Model):
    role_name=m.CharField(max_length=100,null=False)

    def __str__(self):
        return self.role_name

class Departments(m.Model):
    Dept_name=m.CharField(max_length=100,null=False)
    location=m.CharField(max_length=100)

    def __str__(self):
        return self.Dept_name


class Employee(m.Model):
    genders = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    First_name=m.CharField(max_length=100)
    Last_name=m.CharField(max_length=100)
    Department=m.ForeignKey(Departments,on_delete=m.CASCADE)
    Salary=m.IntegerField(default=0)
    Bonus=m.IntegerField(default=0)
    Role=m.ForeignKey(Roles,on_delete=m.CASCADE)
    Phone=m.IntegerField(default=0)
    Hire_date=m.DateField()
    Gender=m.CharField(max_length=10,choices=genders,default="M")


    def __str__(self):
        return "%s %s" %(self.First_name,self.Last_name)
