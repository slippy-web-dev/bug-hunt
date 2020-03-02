from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required
def index(request):
    test_object = { 'test' : 7 }
    return render(request, 'static_files/home.html', context=test_object)

@login_required
def new_bug(request):
    context = { 'message' : 'This is "new bug" link'}
    return render(request, 'static_files/test.html', context=context)

@login_required
def update_bug(request):
    context = { 'message' : 'This is "update bug" link'}
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def database_maintenance(request):
    context = { 'message' : 'This is "database maintenance" page' }
    return render(request, 'static_files/db-maintenance.html', context=context)

@staff_member_required
def edit_add_areas(request):
    context = { 'message' : 'This is "edit/add areas" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def add_programs(request):
    context = { 'message' : 'This is "add programs" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def edit_programs(request):
    context = { 'message' : 'This is "edit programs" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def add_employees(request):
    context = { 'message' : 'This is "add employees" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def edit_employees(request):
    context = { 'message' : 'This is "edit employees" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def export_areas(request):
    context = { 'message' : 'This is "export areas" page' }
    return render(request, 'static_files/test.html', context=context)