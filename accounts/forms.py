from django import forms
from django.contrib.auth import get_user_model
from .models import Teacher, Employee, Student, Department, Specialization

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['phone_number'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email'],
            birth_date=self.cleaned_data['birth_date'],
            password=self.cleaned_data['password'],
        )
        return user


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=16)
    password = forms.CharField(max_length=20)

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'specialization', 'experience', 'salary', 'qualification', 'status']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'department', 'experience', 'salary', 'qualification', 'status']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'parent_contact', 'status']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['name', 'description']