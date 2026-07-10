from django.shortcuts import render, redirect, get_object_or_404
from .forms import DepartmentForm, SpecializationForm, EmployeeForm
from .models import Department, Specialization, Employee

# DEPARTMENT --- CRUD
def get_department(request):
    departments = Department.objects.all()
    return render(request, 'employees/department/department_list.html', {'departments': departments})

def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'employees/department/create_department.html', {'form': form})

def read_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'employees/department/read_department.html', {'department': department})

def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'employees/department/create_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'employees/department/delete_department.html', {'department': department})


# SPECIALIZATION --- CRUD
def get_specialization(request):
    specializations = Specialization.objects.all()
    return render(request, 'employees/specialization/specialization_list.html', {'specializations': specializations})


def create_specialization(request):
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialization_list')
    else:
        form = SpecializationForm()
    return render(request, 'employees/specialization/create_specialization.html', {'form': form})


def read_specialization(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    return render(request, 'employees/specialization/read_specialization.html', {'specialization': specialization})


def update_specialization(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    if request.method == 'POST':
        form = SpecializationForm(request.POST, instance=specialization)
        if form.is_valid():
            form.save()
            return redirect('specialization_list')
    else:
        form = SpecializationForm(instance=specialization)
    return render(request, 'employees/specialization/create_specialization.html', {'form': form})


def delete_specialization(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    if request.method == 'POST':
        specialization.delete()
        return redirect('specialization_list')
    return render(request, 'employees/specialization/delete_specialization.html', {'specialization': specialization})


# EMPLOYEE --- CRUD
def get_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee/employee_list.html', {'employees': employees})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee/create_employee.html', {'form': form})


def read_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee/read_employee.html', {'employee': employee})


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee/create_employee.html', {'form': form})


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee/delete_employee.html', {'employee': employee})
