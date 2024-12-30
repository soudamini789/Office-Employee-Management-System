from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):

    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method =='POST':
        Firstname=request.POST['Firstname']
        Lastname=request.POST['Lastname']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        dept=request.POST['dept']
        role=request.POST['role']
        #firstname=request.POST['firstname']
        new_emp=Employee(Firstname=Firstname,Lastname=Lastname,salary=salary,bonus=bonus,dept_id=dept,role_id=role,hiredate=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
    
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Exception occured')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)

def Filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(Firstname__icontains = name) |Q(Lastname__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'Filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')