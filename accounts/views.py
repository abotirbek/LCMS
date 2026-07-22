from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import EmployeeForm, LoginForm, RegistrationForm, StudentForm, TeacherForm, DepartmentForm, SpecializationForm
from accounts.models import Employee, Student, Teacher, Department, Specialization


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            authenticated_user = authenticate(request, username=user.phone_number, password=form.cleaned_data['password'])
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('center_list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('center_list')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Teacher --- CRUD

def get_teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'accounts/teacher/teacher_list.html', {'teacher': teacher})

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'accounts/teacher/create_teacher.html', {'form': form})

def read_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'accounts/teacher/read_teacher.html', {'teacher': teacher})

def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'accounts/teacher/update_teacher.html', {'form': form})

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'accounts/teacher/delete_teacher.html', {'teacher': teacher})

# Employee --- CRUD

def get_employee(request):
    employee = Employee.objects.all()
    return render(request, 'accounts/employee/employee_list.html', {'employee': employee})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'accounts/employee/create_employee.html', {'form': form})

def read_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'accounts/employee/read_employee.html', {'employee': employee})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'accounts/employee/update_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'accounts/employee/delete_employee.html', {'employee': employee})

# Student --- CRUD

def get_student(request):
    student = Student.objects.all()
    return render(request, 'accounts/student/student_list.html', {'student': student})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'accounts/student/create_student.html', {'form': form})

def read_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'accounts/student/read_student.html', {'student': student})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'accounts/student/update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'accounts/student/delete_student.html', {'student': student})

# Department --- CRUD

def get_department(request):
    department = Department.objects.all()
    return render(request, 'accounts/department/department_list.html', {'department': department})

def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = StudentForm()
    return render(request, 'accounts/department/create_department.html', {'form': form})

def read_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'accounts/department/read_department.html', {'department': department})

def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'accounts/department/update_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'accounts/department/delete_department.html', {'department': department})

# Specialization --- CRUD

def get_specialization(request):
    specialization = Specialization.objects.all()
    return render(request, 'accounts/specialization/specialization_list.html', {'specialization': specialization})

def create_specialization(request):
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialization_list')
    else:
        form = SpecializationForm()
    return render(request, 'accounts/specialization/create_specialization.html', {'form': form})

def read_specialization(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    return render(request, 'accounts/specialization/read_specialization.html', {'specialization': specialization})

def update_specialization(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    if request.method == 'POST':
        form = SpecializationForm(request.POST, instance=specialization)
        if form.is_valid():
            form.save()
            return redirect('specialization_list')
    else:
        form = SpecializationForm(instance=specialization)
    return render(request, 'accounts/specialization/update_specialization.html', {'form': form})

def delete_specialization(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    if request.method == 'POST':
        specialization.delete()
        return redirect('specialization_list')
    return render(request, 'accounts/specialization/delete_specialization.html', {'specialization': specialization})