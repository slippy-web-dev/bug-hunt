from import_export import resources
from .models import Employees, FunctionalAreas, Programs

class EmployeesResource(resources.ModelResource):
    class Meta:
        model = Employees

class FunctionalAreasResource(resources.ModelResource):
    class Meta:
        model = FunctionalAreas

class ProgramsResource(resources.ModelResource):
    class Meta:
        model = Programs
        