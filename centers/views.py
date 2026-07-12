from django.shortcuts import render, get_object_or_404, redirect
from .forms import CenterForm, BranchForm, RoomForm
from .models import Center, Branch, Room


# CENTER --- CRUD
def get_center(request):
    center = Center.objects.all()
    return render(request, 'centers/center/center_list.html', {'center': center})

def create_center(request):
    if request.method == 'POST':
        form = CenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('center_list')
    else:
        form = CenterForm()
    return render(request, 'centers/center/create_center.html', {'form': form})

def read_center(request, pk):
    center = get_object_or_404(Center, pk=pk)
    return render(request, 'centers/center/read_center.html', {'center': center})

def update_center(request, pk):
    center = get_object_or_404(Center, pk=pk)
    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return redirect('center_list')
    else:
        form = CenterForm(instance=center)
    return render(request, 'centers/center/update_center.html', {'form': form})

def delete_center(request, pk):
    center = get_object_or_404(Center, pk=pk)
    if request.method == 'POST':
        center.delete()
        return redirect('center_list')
    else:
        return render(request, 'centers/center/delete_center.html', {'center': center})

# BRANCH --- CRUD

def get_branch(request):
    branch = Branch.objects.all()
    return render(request, 'centers/branch/branch_list.html', {'branch': branch})

def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm()
    return render(request, 'centers/branch/create_branch.html', {'form': form})

def read_branch(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    return render(request, 'centers/branch/read_branch.html', {'branch': branch})

def update_branch(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'centers/branch/update_branch.html', {'form': form})

def delete_branch(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    else:
        return render(request, 'centers/branch/delete_branch.html', {'branch': branch})

# ROOM --- CRUD

def get_room(request):
    room = Room.objects.all()
    return render(request, 'centers/room/room_list.html', {'room': room})

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'centers/room/create_room.html', {'form': form})

def read_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'centers/room/read_room.html', {'room': room})

def update_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'centers/room/update_room.html', {'form': form})

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    else:
        return render(request, 'centers/room/delete_room.html', {'room': room})