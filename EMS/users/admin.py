from django.contrib import admin
from .models import companies,employers,company_profile,employer_profile

class companyform(admin.ModelAdmin):
    list_display=['company_id','email','password','company_name']
admin.site.register(companies,companyform)
class company_profile_form(admin.ModelAdmin):
    list_display=['company_id','address','established_year','ceo','company_logo','contact_no','gst_no','created_at']
admin.site.register(company_profile,company_profile_form)
class employerform(admin.ModelAdmin):
    list_display=['emp_id','name','email','password','company_id']
admin.site.register(employers,employerform)  
class employer_profile_form(admin.ModelAdmin):
    list_display=['emp_id','dob','profile_image','gender','mobile_no','joining_date','company_id','project_id','department_id','created_at']
admin.site.register(employer_profile,employer_profile_form)     