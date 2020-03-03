from django.urls import path
from . import views
from django.contrib.auth import views as django_auth_views

app_name = 'app'
urlpatterns = [
    path('login/', django_auth_views.LoginView.as_view(), name='login'),
    path('logout/', django_auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('new-bug/', views.new_bug, name='new_bug'),
    path('update-bug/', views.update_bug, name='update_bug'),
    path('admin/db-maintenance/', views.database_maintenance, name='database_maintenance'),
    path('admin/edit-areas/', views.edit_areas, name='edit_areas'),
    path('admin/add-areas/', views.add_areas, name='add_areas'),
    path('admin/add-programs/', views.add_programs, name='add_programs'),
    path('admin/edit-programs/', views.edit_programs, name='edit_programs'),
    path('admin/add-employees/', views.add_employees, name='add_employees'),
    path('admin/edit-employees/', views.edit_employees, name='edit_employees'),
    path('admin/export-areas/', views.export_areas, name='export_areas'),
]
