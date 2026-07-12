from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, EnrollmentForm, AttendanceForm
from .models import Student, Enrollment, Attendance


# STUDENT --- CRUD
def get_student(request):
    students = Student.objects.all()
    return render(request, 'students/student/student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student/create_student.html', {'form': form})

def read_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student/read_student.html', {'student': student})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student/update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student/delete_student.html', {'student': student})

# ENROLLMENT --- CRUD
def get_enrollment(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'students/enrollment/enrollment_list.html', {'enrollments': enrollments})

def create_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'students/enrollment/create_enrollment.html', {'form': form})

def read_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    return render(request, 'students/enrollment/read_enrollment.html', {'enrollment': enrollment})

def update_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'students/enrollment/update_enrollment.html', {'form': form})

def delete_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')
    return render(request, 'students/enrollment/delete_enrollment.html', {'enrollment': enrollment})

# ATTENDANCE --- CRUD
def get_attendance(request):
    attendances = Attendance.objects.all()
    return render(request, 'students/attendance/attendance_list.html', {'attendances': attendances})

def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'students/attendance/create_attendance.html', {'form': form})

def read_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    return render(request, 'students/attendance/read_attendance.html', {'attendance': attendance})

def update_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'students/attendance/update_attendance.html', {'form': form})

def delete_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'students/attendance/delete_attendance.html', {'attendance': attendance})