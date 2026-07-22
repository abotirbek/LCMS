from django import forms
from .models import Course, Groups, Module, RoomType, Room, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'duration',
            'price',
            'language',
            'has_certificate'
        ]

class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
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

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'teacher', 'description', 'files', 'status']


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['title', 'description', 'status']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'room_type', 'has_projector', 'has_desk', 'floor', 'branch', 'status']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['start_time', 'stop_time', 'room', 'module', 'status']