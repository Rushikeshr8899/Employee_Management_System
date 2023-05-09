from django.contrib import admin
from django.urls import path,include
from .views import home,Add_Emp,All_Emp,Filter_Emp,Remove_Emp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('Add_Emp/',Add_Emp,name="Add_Emp"),
    path('All_Emp/',All_Emp,name="All_Emp"),
    path('All_Emp/<int:emp_id>',All_Emp,name="All_Emp"),
    path('Filter_Emp',Filter_Emp,name="Filter_Emp"),
    path('Remove_Emp/',Remove_Emp,name="Remove_Emp"),
    path('Remove_Emp/<int:emp_id>',Remove_Emp,name="Remove_Emp"),

]