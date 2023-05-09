from django.contrib import admin
from .models import Employee,Departments,Roles
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("First_name","Last_name","Department","Salary","Role","Phone")
    list_display_links = ("Last_name","First_name")




admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Departments)
admin.site.register(Roles)
