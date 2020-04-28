from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from tablib import Dataset
from django.contrib import messages

from .models import Employees, FunctionalAreas, Programs, AccessLevels, BugReports, ReportTypes, Severities, Status, Priorities, Resolutions
from .resources import EmployeesResource, FunctionalAreasResource, ProgramsResource

import sqlite3, re, json

# Create your views here.
@login_required
def index(request):
    is_admin = request.user.is_staff
    username = request.user.username
    access_level = 0
    try:
        employee_object = Employees.objects.filter(employee_username=username).values()
        username = employee_object[0]['employee_username']
        accesslevel_obj = AccessLevels.objects.filter(accessLevel_id=employee_object[0]['employee_accesslevel_id']).values()
        access_level = accesslevel_obj[0]['accesslevel']
    except Exception as e:
        print(type(e))

    # test_object = { 'test' : 7 }
    context = { 
        'is_admin' : is_admin,
        'username': username,
        'access_level': access_level
         }
    return render(request, 'static_files/home.html', context=context)

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
        if 'update' in request.POST:
            area_object = FunctionalAreas.objects.get(pk=request.POST['area_id'])
            area_object.area = request.POST['area']
            if FunctionalAreas.objects.filter(area=area_object.area, program_id=area_object.program_id).exists():
               messages.add_message(request, messages.INFO, 'Area ' + area_object.area  + " is duplicated") 
            else:
                try:
                    area_object.save()
                    messages.add_message(request, messages.INFO, 'Area ' + area_object.area  + " has been updated", extra_tags='area_update')
                except Exception as e:
                    print(type(e))
            
        elif 'delete' in request.POST:
            area_id = request.POST['area_id']
            area = request.POST['area']
            try :
                FunctionalAreas.objects.filter(area_id=area_id).delete()
            except Exception as e:
                print(type(e))
            messages.add_message(request, messages.INFO, 'Area ' + area  + " has been deleted", extra_tags='area_delete')
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
        if len(request.POST['area']) > 0:
            area_object = FunctionalAreas(area=request.POST['area'], program_id=program_object)
            if FunctionalAreas.objects.filter(area=area_object.area, program_id=program_object).exists():
                messages.error(request, 'Area name is duplicated')
            else:
                try:
                    area_object.save()
                except Exception as e:
                    print(type(e))
        else:
            messages.error(request, 'Area name cannot be empty')
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
    if request.method == 'GET':
        new_program = Programs()
    if request.method == 'POST':
        new_program = Programs(program_name=request.POST['program_name'],
                    program_version=request.POST['program_version'],
                    program_release=request.POST['program_release']
                    )
        if len(request.POST['program_name']) == 0: 
            messages.add_message(request, messages.INFO, 'Program name cannot be empty', extra_tags='program_name_error')
        if len(request.POST['program_version']) == 0:
            messages.add_message(request, messages.INFO, 'Program version cannot be empty', extra_tags='program_version_empty')
        if len(request.POST['program_release']) == 0:
            messages.add_message(request, messages.INFO, 'Proram release cannot be empty', extra_tags='program_release_empty')
        if  len(list(messages.get_messages(request))) == 0:
            if Programs.objects.filter(program_name=new_program.program_name, program_version=new_program.program_version, 
                program_release=new_program.program_release).exists():
                messages.add_message(request, messages.INFO, 'Proram is duplicated', extra_tags='program_release_empty')
            else:
                try:
                    new_program.save()
                except Exception as e:
                    print(type(e))
                messages.add_message(request, messages.INFO, 'Program ' + new_program.program_name + ' has been added successfully', extra_tags='program_add_success')
                new_program = Programs()
    context = {'new_program': new_program}
    return render(request, 'static_files/add-programs.html', context=context)

@staff_member_required
def edit_programs(request):
    if request.method == 'POST':
        if 'edit' in request.POST:
            program_object = Programs.objects.get(pk=request.POST['program_id'])
            program_object.program_name = request.POST['program_name']
            program_object.program_version = request.POST['program_version']
            program_object.program_release = request.POST['program_release']
            if Programs.objects.filter(program_name=program_object.program_name, 
                program_version=program_object.program_version, program_release=program_object.program_release).exists():
                messages.info(request, 'Program ' + program_object.program_name + ' is duplicated')
            else:
                try:
                    program_object.save()
                    messages.info(request, 'Program ' + program_object.program_name + ' has been updated')
                except Exception as e:
                    print(type(e))
        elif 'delete' in request.POST:
            program_id =  int(request.POST['program_id'])
            program_name = str(request.POST['program_name'])
            try: 
                Programs.objects.filter(program_id=program_id).delete()
            except Exception as e:
                print(type(e)) 
            messages.add_message(request, messages.INFO, 'Program ' + program_name + " has been deleted", extra_tags='program_delete')
        # when save() is successful
    program_list = Programs.objects.all()
    context = { 'message' : 'This is "edit programs" page',
                'program_list' : program_list,
              }
    return render(request, 'static_files/edit-programs.html', context=context)

@staff_member_required
def add_employees(request):
    if request.method == 'GET':
        new_employee = Employees()
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
        if len(request.POST['employee_name']) == 0:
            messages.add_message(request, messages.INFO, "Employee name must not be empty",extra_tags='employee_name_empty')
        if len(request.POST['employee_username']) == 0:
            messages.add_message(request, messages.INFO, "Employee username must not be empty",extra_tags='employee_username_error')
        if len(request.POST['employee_password']) == 0:
            messages.add_message(request, messages.INFO, "Employee password must not be empty",extra_tags='employee_password_empty')
        if User.objects.filter(username=new_employee.employee_username).exists():
            messages.add_message(request, messages.INFO, "This username has been registered", extra_tags='employee_username_error') 
        if len(list(messages.get_messages(request))) == 0: 
            # new_employee.entry_set.add(this_access_level) 
            try:
                new_user = User.objects.create_user(username=request.POST['employee_username'],
                                                    password=request.POST['employee_password'],
                                                    first_name=request.POST['employee_name'],
                                                    is_staff=is_staff
                                                )
                new_employee.save()
            except Exception as e:
                print(type(e))
            messages.add_message(request, messages.INFO, 
                "Employee's username" + new_employee.employee_username + " has been added successfully",
                extra_tags='employee_add_success')
            new_employee = Employees()
    context = { 'message' : 'This is "add employees" page',
                'new_employee': new_employee,
                }
    return render(request, 'static_files/add-employees.html', context=context)

@staff_member_required
def edit_employees(request):
    if request.method == 'POST':
        if 'edit' in request.POST:
            is_staff = False
            if request.POST['accesslevels'] == '3':
                is_staff = True
            this_access_level = AccessLevels.objects.get(accesslevel=request.POST['accesslevels'])
            employee_object = Employees.objects.get(pk=request.POST['employee_id'])
            user_lookup_name = employee_object.employee_username
            employee_message_info = {
                'employee_name' : employee_object.employee_name,
                'employee_username' : employee_object.employee_username,
                'employee_password' : '[Encrypted]',
                'accesslevels' : employee_object.employee_accesslevel.accesslevel
            }
            employee_object.employee_name = request.POST['employee_name']
            employee_object.employee_username = request.POST['employee_username']
            employee_object.employee_password = request.POST['employee_password']
            employee_object.employee_accesslevel = this_access_level

            
            user_object = User.objects.get(username=user_lookup_name)
            user_object.first_name = request.POST['employee_name']
            user_object.username = request.POST['employee_username']
            user_object.set_password(request.POST['employee_password'])
            user_object.is_staff = is_staff
            username_exists = Employees.objects.filter(employee_username=employee_object.employee_username).exists()
            username_change = employee_message_info['employee_username'] != employee_object.employee_username
            print("exist", username_exists)
            print("change", username_change)
            if username_exists and username_change:
                messages.add_message(request, messages.INFO, "Employee username is duplicated", extra_tags='employee_name_update')
            else:
                try:
                    employee_object.save()
                    user_object.save()
                    # when save() is successful
                    messages.info(request, 'Employee ' + user_lookup_name + ' has been updated')
                    messages.add_message(
                        request, 
                        messages.INFO, 
                        'Name: ' + employee_message_info['employee_name'] + ' -> ' + employee_object.employee_name, 
                        extra_tags='employee_name_update'
                    )
                    messages.add_message(
                        request,
                        messages.INFO,
                        'Username: ' + employee_message_info['employee_username'] + ' -> ' + employee_object.employee_username,
                        extra_tags='employee_username_update'
                    )
                    messages.add_message(
                        request,
                        messages.INFO,
                        'Password: ' + employee_message_info['employee_password'],
                        extra_tags='employee_password_update'
                    )
                    messages.add_message(
                        request,
                        messages.INFO,
                        'Access Level: ' + employee_message_info['accesslevels'] + ' -> ' + request.POST['accesslevels'],
                        extra_tags='accesslevels_update'
                    )
                except Exception as e:
                    print(type(e))

        elif 'delete' in request.POST:
            employee_object = Employees.objects.get(pk=request.POST['employee_id'])
            employee_id =  int(request.POST['employee_id'])
            try: 
                Employees.objects.filter(employee_id=employee_id).delete()
                User.objects.filter(username=employee_object.employee_username).delete()
            except Exception as e:
                print(type(e)) 
            messages.add_message(request,
                messages.INFO,
                'User ' + employee_object.employee_username + " has been deleted",
                extra_tags='employee_delete')

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
            which_table = 'INSERT INTO "app_employees"'
        elif db_table == 'Programs':
            table_object = Programs.objects.all()
            program_resource = ProgramsResource()
            dataset = program_resource.export()
            which_table = 'INSERT INTO "app_programs"'
        elif db_table == 'Areas':
            table_object = FunctionalAreas.objects.all()
            area_resource = FunctionalAreasResource()
            dataset = area_resource.export()
            which_table = 'INSERT INTO "app_functionalareas"'
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
            f = open(db_table + '.xml', 'w')
            my_file = File(f)
            my_file.write(data)
            my_file.close()
            context = { 'message' : 'XML successfully exported!' }
        elif file_format == 'ASCII':
            import sqlite3, os
            project_root_dir = os.getcwd()
            con = sqlite3.connect(project_root_dir + '/db.sqlite3')
            with open(db_table + '.txt', 'w') as f:
                for line in con.iterdump():
                    if line.startswith(which_table):
                        f.write('%s\n' % line)
            con.close()
        elif file_format == 'ASCII_old':
            con = sqlite3.connect('db.sqlite3')
            with open('exported_data.txt', 'w') as f:
                for line in con.iterdump():
                    # edit LINE to fit with SQL format
                    if any(invalid_stmt in line for invalid_stmt in ['BEGIN TRANSACTION','COMMIT','sqlite_sequence','CREATE UNIQUE INDEX']): 
                        continue
                    else:
                        m = re.search('CREATE TABLE "([a-z_]*)"(.*)', line)
                        if m :
                            name, sub = m.groups()
                            sub = sub.replace('"','`')
                            line = '''DROP TABLE IF EXISTS %(name)s; CREATE TABLE IF NOT EXISTS %(name)s%(sub)s'''
                            line = line % dict(name=name, sub=sub)
                        else:
                            m = re.search('INSERT INTO "([a-z_]*)"(.*)', line)
                            if m:
                                line = 'INSERT INTO %s%s\n' % m.groups()
                                line = line.replace('"', r'\"')
                                line = line.replace('"', "'")
                        line = re.sub(r"([^'])'t'(.)", r"\1THIS_IS_TRUE\2", line)
                        line = line.replace('THIS_IS_TRUE', '1')
                        line = re.sub(r"([^'])'f'(.)", r"\1THIS_IS_FALSE\2", line)
                        line = line.replace('THIS_IS_FALSE', '0')
                        line = line.replace('AUTOINCREMENT', 'AUTO_INCREMENT')
                        line = line.replace('app_', '')
                        f.write('%s\n' % line)
        else:
            context = { 'message' : 'Please type in one of the following choices: CSV, JSON, XLS (Excel), XML'}
            return render(request, 'static_files/export.html', context=context)
    return render(request, 'static_files/export.html', context=context)

@login_required
def new_bug(request):
    # get all lists for dropdown
    program_list = Programs.objects.all()
    report_type_list = ReportTypes.objects.all()
    severity_list = Severities.objects.all()
    employee_list = Employees.objects.all()
    default_report_by = str(request.user)
    area_list = FunctionalAreas.objects.all()
    status_list = Status.objects.all()
    priority_list = Priorities.objects.all()
    resolution_list = Resolutions.objects.all()
    new_bug = BugReports()
    if request.method == 'POST':
        # extract request
        isReproduciple = request.POST.get('reproducible', False) == 'on'
        isDeferred = request.POST.get('deferred', False) == 'on'
        program_id = request.POST.get('program', False)
        report_type_id = request.POST.get('report', False)
        severity_id = request.POST.get('severity', False)
        summary = request.POST.get('summary', False)
        description = request.POST.get('problem', False)
        suggested_fix = request.POST.get('suggest_fix', False)
        reported_by = request.POST.get('reported_by', False)
        date_report = request.POST.get('date_report', False)
        area_id = request.POST.get('area', False)
        assigned_to = request.POST.get('assigned_to', False)
        comment = request.POST.get('comment', False)
        status_id = request.POST.get('status', False)
        priority_id = request.POST.get('priority', False)
        resolution_id = request.POST.get('resolution', False)
        resolution_version = request.POST.get('resolution_version', False)
        resolved_by = request.POST.get('resolved_by', False)
        date_resolved = request.POST.get('date_resolved', False)
        tested_by = request.POST.get('tested_by', False)
        date_tested = request.POST.get('date_tested', False)

        # Validate Field
        if not program_id: messages.add_message(request, messages.INFO, 'Program; ')
        else: new_bug.program_id = Programs.objects.only('program_id').get(program_id=program_id)

        if not report_type_id: messages.add_message(request, messages.INFO, 'Report Type; ')
        else: new_bug.type_id = ReportTypes.objects.only('report_type_id').get(report_type_id=report_type_id)

        if not severity_id: messages.add_message(request, messages.INFO, 'Severity; ')
        else: new_bug.severity_id = Severities.objects.only('severity_id').get(severity_id=severity_id)

        if not summary: messages.add_message(request, messages.INFO, 'Summary; ')
        else: new_bug.summary = summary
            
        if not description: messages.add_message(request, messages.INFO, 'Description; ')
        else: new_bug.description = description

        if not suggested_fix: messages.add_message(request, messages.INFO, 'Suggested Fix; ')
        else: new_bug.suggested_fix = suggested_fix

        if not reported_by: messages.add_message(request, messages.INFO, 'Reported Employee; ')
        else: new_bug.reported_by_emp_id=Employees.objects.only('employee_id').get(employee_id=reported_by)

        if not date_report: messages.add_message(request, messages.INFO, 'Reported Date; ')    
        else: new_bug.reported_on_date = date_report

        if area_id: new_bug.functional_area = FunctionalAreas.objects.only('area_id').get(area_id=area_id)

        if assigned_to: new_bug.assigned_to_emp_id = Employees.objects.only('employee_id').get(employee_id=assigned_to)

        if comment: new_bug.comments = comment

        if status_id: new_bug.status = Status.objects.only('status_id').get(status_id=status_id)

        if priority_id: new_bug.priority = Priorities.objects.only('priority_id').get(priority_id=priority_id)

        if resolution_id: new_bug.resolution = Resolutions.objects.only('resolution_id').get(resolution_id=resolution_id)

        if resolution_version: new_bug.resolution_version = Resolutions.objects.only('resolution_id').get(resolution_id=resolution_version)

        if resolved_by: new_bug.resolved_by_emp_id = Employees.objects.only('employee_id').get(employee_id=resolved_by)

        if date_resolved: new_bug.resolved_on_date = date_resolved

        if tested_by: new_bug.tested_by_emp_id = Employees.objects.only('employee_id').get(employee_id=tested_by)

        if date_tested: new_bug.tested_on_date=date_tested

        new_bug.reproducable = isReproduciple
        new_bug.treat_as_deferred = isDeferred

        if len(list(messages.get_messages(request))) == 0:
            try:
                new_bug.save()
                messages.add_message(request,
                    messages.INFO,
                    'New bug is added sucessfully',
                    extra_tags='bug_add_success')
                new_bug = BugReports()
            except Exception as e:
                print("Something went wrong")
                print(type(e))
    context = { 'message' : 'This is "add new bug" page',
    'programs': program_list,
    'report_type': report_type_list,
    'severity': severity_list,
    'employees': employee_list,
    'areas': area_list,
    'status': status_list,
    'priority': priority_list,
    'resolution': resolution_list,
    'new_bug': new_bug}
    return render(request, 'static_files/add-bugs.html', context=context)

def load_areas(request):
    program_id = request.GET.get('program_id')
    area_list = FunctionalAreas.objects.filter(program_id=program_id).values()
    return JsonResponse({"areas": list(area_list)})