from django import forms
from .models import Student, Enrollment, Attendance
from common.forms import CommonIndividualsForm


class StudentForm(CommonIndividualsForm):
    class Meta(CommonIndividualsForm.Meta):
        model = Student
        fields = [
            'name',
            'last_name',
            'birth_date',
            'phone_number',
            'email',
            'enrollment_date',
            'parent_contact',
            'address',
        ]


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = [
            'group',
            'student',
            'enrolled_at',
            'status',
        ]


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'enrollment',
            'lesson_date',
            'status',
        ]