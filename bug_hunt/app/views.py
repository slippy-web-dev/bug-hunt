from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    test_object = { 'test' : 7 }
    return render(request, 'static_files/home.html', context=test_object)
    # return HttpResponse("Index of app")

def new_bug(request):
    context = { 'message' : 'This is "new bug" link'}
    return render(request, 'static_files/test.html', context=context)

def update_bug(request):
    context = { 'message' : 'This is "update bug" link'}
    return render(request, 'static_files/test.html', context=context)

def database_maintenance(request):
    context = { 'message' : 'This is "database maintenance" page' }
    return render(request, 'static_files/db-maintenance.html', context=context)

def edit_add_areas(request):
    context = { 'message' : 'This is "edit/add areas" page' }
    return render(request, 'static_files/test.html', context=context)

def add_programs(request):
    context = { 'message' : 'This is "add programs" page' }
    return render(request, 'static_files/test.html', context=context)

def edit_programs(request):
    context = { 'message' : 'This is "edit programs" page' }
    return render(request, 'static_files/test.html', context=context)

def add_employees(request):
    context = { 'message' : 'This is "add employees" page' }
    return render(request, 'static_files/test.html', context=context)

def edit_employees(request):
    context = { 'message' : 'This is "edit employees" page' }
    return render(request, 'static_files/test.html', context=context)

def export_areas(request):
    context = { 'message' : 'This is "export areas" page' }
    return render(request, 'static_files/test.html', context=context)