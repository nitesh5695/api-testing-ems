from rest_framework import  serializers
from .models import Department, Leave,Project,Salary,Attendance,Department_company
from users.models import employers

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields="__all__"
        
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Salary
        fields="__all__"   

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"
        extra_kwargs = {
           
            'request': {'read_only': True}
        }
class company_department_serializer(serializers.ModelSerializer):
    class Meta:
        model=Department_company
        fields="__all__"
             
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance  
        fields="__all__"             