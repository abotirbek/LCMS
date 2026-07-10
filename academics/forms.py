from django import forms
from .models import Course, Group

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'duration',
            'price',
            'language',
            'certificate_available'
        ]

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'title',
            'start_time',
            'end_time',
            'schedule',
            'capacity',
            'branch',
            'teacher',
            'course'
        ]