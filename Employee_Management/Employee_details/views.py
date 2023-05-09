from django.shortcuts import render, HttpResponse
from .models import Employee,Roles,Departments
from datetime import datetime
from django.db.models import Q
def home(request):
    return  render(request,'index.html')

def Add_Emp(request):
    if request.method=="POST":
        First_name=request.POST.get("First_name")
        Last_name = request.POST.get("Last_name")
        Department = int(request.POST.get("Department"))
        Salary = int(request.POST.get("Salary"))
        Bonus = int(request.POST.get("Bonus"))
        Role = int(request.POST.get("Role"))
        Phone = int(request.POST.get("Phone"))
        Hire_date = request.POST.get("Hire_date")
        data=Employee(First_name=First_name,Last_name=Last_name,Department_id=Department,Salary=Salary,Bonus=Bonus,Role_id=Role,Phone=Phone,Hire_date=datetime.now())
        data.save()
        return render(request,'Add_Emp.html')

    else:
        return  render(request,'Add_Emp.html')

def All_Emp(request):
    employee=Employee.objects.all()
    dept=Departments.objects.all()
    context={
        "emp" : employee,
        "emp1" : dept
    }
    return render(request,'All_Emp.html',context)

def Filter_Emp(request):
    if request.method=="POST":
        name=request.POST['name']
        Department=request.POST['Department']
        Role=request.POST['Role']
        # Gender=request.POST["Gender"]
        emp=Employee.objects.all()

        if name:
            emp=emp.filter(Q(First_name__icontains=name) | Q(Last_name__icontains=name))
        if Department:
            emp=emp.filter(Department__Dept_name = Department)
        if Role:
            emp=emp.filter(Role__role_name = Role)

        context={
            "emp":emp
        }
        return  render(request,'All_Emp.html',context)

    return render(request, 'Filter_Emp.html')

def Remove_Emp(request,emp_id=0):
    if emp_id:
        emp_del=Employee.objects.get(id=emp_id)
        emp_del.delete()
        return render(request,'Remove_Emp.html')

    employee = Employee.objects.all()
    context = {
        "emp": employee
    }
    return  render(request,'Remove_Emp.html',context)


