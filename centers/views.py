from django.shortcuts import render, get_object_or_404, redirect
from .forms import CenterForm, BranchForm
from .models import Centers, Branch


# CENTER --- CRUD
def get_center(request):
    center = Centers.objects.all()
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
    center = get_object_or_404(Centers, pk=pk)
    return render(request, 'centers/center/read_center.html', {'center': center})

def update_center(request, pk):
    center = get_object_or_404(Centers, pk=pk)
    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return redirect('center_list')
    else:
        form = CenterForm(instance=center)
    return render(request, 'centers/center/update_center.html', {'form': form})

def delete_center(request, pk):
    center = get_object_or_404(Centers, pk=pk)
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

def get_statistics(request):
    data = Centers.objects.count()
    return render(request, 'centers/statistics.html', {'data': data})