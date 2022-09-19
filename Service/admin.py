from wsgiref.simple_server import demo_app
from django.contrib import admin
from .models import Department, Subject, CutOff, Service, Faculty
from .data import Data, AspirantData

class SubjectAdmin(admin.StackedInline):
    model = Subject
    extra = 4
    
class CutOffAdmin(admin.StackedInline):
    model = CutOff
    extra = 1
    
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [SubjectAdmin, CutOffAdmin]

class DepartmentFaculty(admin.StackedInline):
    model = Department
    extra = 3

class FacultyAdmin(admin.ModelAdmin):
    inlines = [DepartmentFaculty]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject)
admin.site.register(CutOff)
admin.site.register(Service)
admin.site.register(Data)
admin.site.register(AspirantData)
admin.site.register(Faculty, FacultyAdmin)

