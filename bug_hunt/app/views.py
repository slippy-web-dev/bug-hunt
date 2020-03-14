from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from tablib import Dataset

from .models import Employees, FunctionalAreas, Programs, AccessLevels
from .resources import EmployeesResource, FunctionalAreasResource, ProgramsResource

# Create your views here.
@login_required
def index(request):
    is_admin = request.user.is_staff
    # test_object = { 'test' : 7 }
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
        area_object = FunctionalAreas.objects.get(pk=request.POST['area_id'])
        area_object.area = request.POST['area']
        area_object.save()
        program_id = request.POST['program_id']
        program_object = Programs.objects.get(pk=program_id)
        area_list = FunctionalAreas.objects.filter(program_id=program_id)
        context = { 'program' : program_object,
                    'area_list' : area_list,
                  }
        return render(request, 'static_files/add-areas.html', context=context)
    else:
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
        area_list = FunctionalAreas.objects.filter(program_id=request.POST['program_id'])
        context = { 'program' : program_object,
                    'area_list' : area_list,
                  }
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
    if request.method == 'POST':
        program_object = Programs.objects.get(pk=request.POST['program_id'])
        program_object.program_name = request.POST['program_name']
        program_object.program_version = request.POST['program_version']
        program_object.program_release = request.POST['program_release']
        program_object.save()
    program_list = Programs.objects.all()
    context = { 'message' : 'This is "edit programs" page',
                'program_list' : program_list,
              }
    return render(request, 'static_files/edit-programs.html', context=context)

@staff_member_required
def add_employees(request):
    if request.method == 'POST':
        is_staff = False
        if request.POST['accesslevels'] == '3':
            is_staff = True
        this_access_level = AccessLevels.objects.get(accesslevel=request.POST['accesslevels'])
        new_employee = Employees(employee_name=request.POST['employee_name'],
                                 employee_username=request.POST['employee_username'],
                                 employee_password=request.POST['employee_password'],
                                 employee_accesslevel=this_access_level
                                )
        # new_employee.entry_set.add(this_access_level)
        new_user = User.objects.create_user(username=request.POST['employee_username'],
                                            password=request.POST['employee_password'],
                                            first_name=request.POST['employee_name'],
                                            is_staff=is_staff
                                           )
        new_user = User(first_name=request.POST['employee_name'],
                        username=request.POST['employee_username'],
                        password=request.POST['employee_password'],
                        is_staff=is_staff
                       )
        new_employee.save()
    context = { 'message' : 'This is "add employees" page' }
    return render(request, 'static_files/add-employees.html', context=context)

@staff_member_required
def edit_employees(request):
    if request.method == 'POST':
        is_staff = False
        if request.POST['accesslevels'] == '3':
            is_staff = True
        this_access_level = AccessLevels.objects.get(accesslevel=request.POST['accesslevels'])
        employee_object = Employees.objects.get(pk=request.POST['employee_id'])
        user_lookup_name = employee_object.employee_name
        employee_object.employee_name = request.POST['employee_name']
        employee_object.employee_username = request.POST['employee_username']
        employee_object.employee_password = request.POST['employee_password']
        employee_object.employee_accesslevel = this_access_level

        user_object = User.objects.get(first_name=user_lookup_name)
        user_object.first_name = request.POST['employee_name']
        user_object.username = request.POST['employee_username']
        user_object.set_password(request.POST['employee_password'])
        user_object.is_staff = is_staff
        employee_object.save()
        user_object.save()
    employee_list = Employees.objects.all()
    context = { 'message' : 'This is "edit employees" page',
                'employee_list' : employee_list,
              }
    return render(request, 'static_files/edit-employees.html', context=context)

@staff_member_required
def export_areas(request):
    context = { 'message' : 'This is "export areas" page' }
    return render(request, 'static_files/test.html', context=context)

@staff_member_required
def export_data(request):
    context = {}
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file_format']
        db_table = request.POST['db_table']
        if db_table == 'Employees':
            table_object = Employees.objects.all()
            employee_resource = EmployeesResource()
            dataset = employee_resource.export()
        elif db_table == 'Programs':
            table_object = Programs.objects.all()
            program_resource = ProgramsResource()
            dataset = program_resource.export()
        elif db_table == 'FunctionalAreas':
            table_object = FunctionalAreas.objects.all()
            area_resource = FunctionalAreasResource()
            dataset = area_resource.export()
        else:
            context = { 'message' : 'Please type in "Employees", "Programs", or "FunctionalAreas"'}
            return render(request, 'static_files/export.html', context=context)

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response
        elif file_format == 'XML':
            from django.core import serializers
            data = serializers.serialize('xml', table_object)
            from django.core.files import File
            f = open('exported_data.xml', 'w')
            my_file = File(f)
            my_file.write(data)
            my_file.close()
            context = { 'message' : 'XML successfully exported!' }
        else:
            context = { 'message' : 'Please type in one of the following choices: CSV, JSON, XLS (Excel), XML'}
            return render(request, 'static_files/export.html', context=context)
    return render(request, 'static_files/export.html', context=context)