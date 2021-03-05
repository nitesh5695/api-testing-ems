from django.contrib import admin
from .models import Attendance, Department_company, Project, Salary,Leave,Department


class salary(admin.ModelAdmin):
    list_display=['salary_id','emp_id','company_id','paid_date','month','salary','created_at']
admin.site.register(Salary,salary)    

class leave(admin.ModelAdmin):
    list_display=['leave_id','emp_id','status','from_date','to_date','leave_type','subject','reason','apply_date','created_at','modified_at']
admin.site.register(Leave,leave)    
class project(admin.ModelAdmin):
    list_display=['project_id','company_id','title','start_date','end_date','project_leader','status','created_at','modified_at']
admin.site.register(Project,project)    
class department(admin.ModelAdmin):
    list_display=['dept_id','department_name','request','created_by','created_at']
admin.site.register(Department,department)    
class department_company(admin.ModelAdmin):
    list_display=['id','company_id','dept_id']
admin.site.register(Department_company,department_company)    
class attendance(admin.ModelAdmin):
    list_display=['attendance_id','emp_id','company_id','date','status']
admin.site.register(Attendance,attendance)    