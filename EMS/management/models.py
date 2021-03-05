
from django.db import models
import datetime

from users.models import companies, employers




choice = (
    ('accept', 'accept'),
    ('reject', 'reject')
)
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    request = models.CharField(max_length = 10, choices=choice, default = 'pending')
    created_at = models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=300)
    def __str__(self):
        return self.department_name

class Department_company(models.Model):
    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    company_id = models.ForeignKey(companies, on_delete=models.CASCADE)       



class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(employers, on_delete=models.CASCADE)
    company_id=models.ForeignKey(companies,on_delete=models.CASCADE)
    type_choice = (
    ("General", 'General'),
    ('Annual', 'Annual'),
    ('Emergency','Emergency'),
    ('Special','Special'))
    leave_type = models.CharField(max_length=10, choices=type_choice, default='general')
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(default=datetime.date.today)
    reason = models.TextField(max_length=1200)
    subject=models.CharField(max_length=500,null=False)
    created_at = models.DateField(default=datetime.date.today)
    modified_at=models.DateField(default=datetime.date.today)
    apply_date=models.DateField(auto_now_add=True)
    choice = (
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    ('Pending','Pending')
)
    status = models.CharField(max_length=10, choices=choice, default='Pending')


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(companies, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    client_name=models.CharField(max_length=300)
    project_leader=models.CharField(max_length=300)
    start_date=models.DateField(default=datetime.date.today)
    end_date=models.DateField()
    status_choice=(
        ('On Hold','On Hold'),
        ('Cancelled','Cancelled'),
        ('Completed','Completed')

    )
    modified_at=models.DateField(default=datetime.date.today)
    created_at=models.DateField(auto_now_add=True)

    status= models.CharField(max_length=20, choices=status_choice, default='On Hold')

class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(employers, on_delete=models.CASCADE)
    company_id=models.ForeignKey(companies,on_delete=models.CASCADE)
    paid_date = models.DateField(default=datetime.date.today)
    description=models.TextField(max_length=1200,null=True,blank=True)
    months=(
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')
    )
    month = models.CharField(max_length=12,choices=months,null=False)
    salary = models.IntegerField()
    created_at=models.DateField(auto_now_add=True)

class Attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    emp_id=models.ForeignKey(employers,on_delete=models.CASCADE)
    company_id=models.ForeignKey(companies,on_delete=models.CASCADE)
    date=models.DateField()
    attend_choice=(
        ('Present','Present'),
        ('Absent','Absent')
    )
    status=models.CharField(max_length=10,choices=attend_choice)    
