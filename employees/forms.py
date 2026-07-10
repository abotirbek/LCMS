from django import forms
from common.forms import CommonIndividualsForm
from .models import Department, Specialization, Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['name']


class EmployeeForm(CommonIndividualsForm):
    class Meta(CommonIndividualsForm.Meta):
        model = Employee
        fields = [
            'name',
            'last_name',
            'birth_date',
            'phone_number',
            'email',
            'hire_date',
            'salary',
            'qualification',
            'specialization',
            'department',
        ]