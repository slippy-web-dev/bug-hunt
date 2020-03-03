from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .models import Employees, FunctionalAreas, Programs, AccessLevels

# Create your views here.
@login_required
def index(request):
    is_admin = request.user.is_staff
    test_object = { 'test' : 7 }
    context = { 'is_admin' : is_admin }
    return render(request, 'static_files/home.html', context=context)

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
def edit_areas(request):
    if request.method == 'POST':
        print ("")
    program_list = Programs.objects.all()
    context = { 'message' : 'This is "edit/add areas" page' ,
                'program_list' : program_list,
              }
    return render(request, 'static_files/edit-areas.html', context=context)

@staff_member_required
def add_areas(request):
    if request.method == 'POST':
        program_object = Programs.objects.get(pk=request.POST['program_id'])
        area_object = FunctionalAreas(area=request.POST['area'],
                                    program_id=program_object
                                   )
        area_object.save()
        context = {}
    elif request.method == 'GET':
        program_id = request.GET.get('program_id')
        program_object = Programs.objects.get(pk=program_id)
        area_list = FunctionalAreas.objects.filter(program_id=program_id)
        context = { 'message' : 'This is "add areas" page',
                    'area_list' : area_list,
                    'program' : program_object,
                  }
    return render(request, 'static_files/add-areas.html', context=context)

@staff_member_required
def add_programs(request):
    program_list = Programs.objects.all()
    context = { 'message' : 'This is "add programs" page',
                'program_list' : program_list,
              }
    if request.method == 'POST':
        new_program = Programs(program_name=request.POST['program_name'],
                               program_version=request.POST['program_version'],
                               program_release=request.POST['program_release']
                              )
        new_program.save()
    return render(request, 'static_files/add-programs.html', context=context)

@staff_member_required
def edit_programs(request):
    context = { 'message' : 'This is "edit programs" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def add_employees(request):
    if request.method == 'POST':
        this_access_level = AccessLevels.objects.get(accesslevel=request.POST['accesslevels'])
        new_employee = Employees(employee_name=request.POST['employee_name'],
                                 employee_username=request.POST['employee_username'],
                                 employee_password=request.POST['employee_password'],
                                 employee_access_level=this_access_level
                                )
    context = { 'message' : 'This is "add employees" page' }
    return render(request, 'static_files/add-employees.html', context=context)

@staff_member_required
def edit_employees(request):
    context = { 'message' : 'This is "edit employees" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def export_areas(request):
    context = { 'message' : 'This is "export areas" page' }
    return render(request, 'static_files/test.html', context=context)