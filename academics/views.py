from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Group
from .forms import CourseForm, GroupForm

# COURSE --- CRUD

def get_course(request):
    course = Course.objects.all()
    return render(request, 'academics/course/course_list.html', {'course': course})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'academics/course/create_course.html', {'form': form})

def read_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'academics/course/read_course.html', {'course': course})

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'academics/course/update_course.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    else:
        return render(request, 'academics/course/delete_course.html', {'course': course})

# GROUP --- CRUD

def get_group(request):
    group = Group.objects.all()
    return render(request, 'academics/group/group_list.html', {'group': group})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'academics/group/create_group.html', {'form': form})

def read_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'academics/group/read_group.html', {'group': group})

def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'academics/group/update_group.html', {'form': form})

def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    else:
        return render(request, 'academics/group/delete_group.html', {'group': group})