from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Groups
from .forms import CourseForm, GroupForm

# COURSE --- CRUD

def get_course(request):
    course = Course.objects.all()
    return render(request, 'education/course/course_list.html', {'course': course})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'education/course/create_course.html', {'form': form})

def read_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'education/course/read_course.html', {'course': course})

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'education/course/update_course.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    else:
        return render(request, 'education/course/delete_course.html', {'course': course})

# GROUP --- CRUD

def get_group(request):
    group = Group.objects.all()
    return render(request, 'education/group/group_list.html', {'group': group})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'education/group/create_group.html', {'form': form})

def read_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'education/group/read_group.html', {'group': group})

def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'education/group/update_group.html', {'form': form})

def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    else:
        return render(request, 'education/group/delete_group.html', {'group': group})

# MODULE --- CRUD

def get_module(request):
    module = Module.objects.all()
    return render(request, 'lesson/module/module_list.html', {'module': module})


def create_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm()
    return render(request, 'lesson/module/create_module.html', {'form': form})


def read_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    return render(request, 'lesson/module/read_module.html', {'module': module})


def update_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm(instance=module)
    return render(request, 'lesson/module/update_module.html', {'form': form})


def delete_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('module_list')
    else:
        return render(request, 'lesson/module/delete_module.html', {'module': module})


# ROOM TYPE --- CRUD

def get_room_type(request):
    room_type = RoomType.objects.all()
    return render(request, 'lesson/room_type/room_type_list.html', {'room_type': room_type})


def create_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_type_list')
    else:
        form = RoomTypeForm()
    return render(request, 'lesson/room_type/create_room_type.html', {'form': form})


def read_room_type(request, pk):
    room_type = get_object_or_404(RoomType, pk=pk)
    return render(request, 'lesson/room_type/read_room_type.html', {'room_type': room_type})


def update_room_type(request, pk):
    room_type = get_object_or_404(RoomType, pk=pk)
    if request.method == 'POST':
        form = RoomTypeForm(request.POST, instance=room_type)
        if form.is_valid():
            form.save()
            return redirect('room_type_list')
    else:
        form = RoomTypeForm(instance=room_type)
    return render(request, 'lesson/room_type/update_room_type.html', {'form': form})


def delete_room_type(request, pk):
    room_type = get_object_or_404(RoomType, pk=pk)
    if request.method == 'POST':
        room_type.delete()
        return redirect('room_type_list')
    else:
        return render(request, 'lesson/room_type/delete_room_type.html', {'room_type': room_type})


# ROOM --- CRUD

def get_room(request):
    room = Room.objects.all()
    return render(request, 'lesson/room/room_list.html', {'room': room})


def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'lesson/room/create_room.html', {'form': form})


def read_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'lesson/room/read_room.html', {'room': room})


def update_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'lesson/room/update_room.html', {'form': form})


def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    else:
        return render(request, 'lesson/room/delete_room.html', {'room': room})


# LESSON --- CRUD

def get_lesson(request):
    lesson = Lesson.objects.all()
    return render(request, 'lesson/lesson/lesson_list.html', {'lesson': lesson})


def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'lesson/lesson/create_lesson.html', {'form': form})


def read_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lesson/lesson/read_lesson.html', {'lesson': lesson})


def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lesson/lesson/update_lesson.html', {'form': form})


def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    else:
        return render(request, 'lesson/lesson/delete_lesson.html', {'lesson': lesson})
