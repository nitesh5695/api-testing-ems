from django.db import models
#from management.models import Project,Department
import datetime


class companies(models.Model):
    company_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=300,unique=True)
    password=models.CharField(max_length=200,null=False)
    company_name=models.CharField(max_length=300,null=False)
    def __str__(self):
        return str(self.company_id)

class company_profile(models.Model):
    def nameFile(instance, filename):
      return '/'.join(['images', str(instance.company_id), filename])
    company_id=models.OneToOneField(companies,on_delete=models.CASCADE ,primary_key=True) 
    address=models.CharField(max_length=600)
    established_year=models.CharField(max_length=4)
    ceo=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=13)
    gst_no=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to=nameFile,blank=True)
    modified_at=models.DateField(default=datetime.date.today)
    created_at=models.DateField(auto_now_add=True,blank=True)


class employers(models.Model):
    emp_id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=300,unique=True)
    name=models.CharField(max_length=250)
    password=models.CharField(max_length=200,null=True)
    company_id=models.ForeignKey(companies,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.email

class employer_profile(models.Model):
    def nameFile(instance, filename):
      return '/'.join(['images', str(instance.company_id), filename])
    emp_id=models.OneToOneField(employers,on_delete=models.CASCADE,primary_key=True)
    dob=models.DateField()
    choice=(
        ("Male","Male"),
        ("Female","Female"),
        ("others","others")
    )
    gender=models.CharField(max_length=10,choices=choice)
    address=models.CharField(max_length=600,blank=True)
    mobile_no=models.CharField(max_length=13,blank=True)
    joining_date=models.DateField()
    profile_image=models.ImageField(upload_to=nameFile,blank=True)
    company_id=models.ForeignKey(companies,on_delete=models.CASCADE)
    project_id=models.ForeignKey(to='management.Project',on_delete=models.CASCADE,null=True)
    department_id=models.ForeignKey(to='management.Department',on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    add_role=models.CharField(max_length=300,blank=True,null=True)
    job_choice=(
        ('Full Time','Full_time'),
        ('Part Time','Part_time'),
        ('Training','Training')
    )
    job_type=models.CharField(max_length=13,choices=job_choice)
    status_choice=(
        ('Active','Active'),
        ('Inactive','Inactive')
    )
    status=models.CharField(max_length=11,choices=status_choice)




