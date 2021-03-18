
from rest_framework import  serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import (Department, Leave,Project,Salary,
Attendance,Department_company,PA_Phases,phases_question,review,choices)
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

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=phases_question
        fields="__all__"     
class PhaseSerializer(WritableNestedModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model=PA_Phases
        fields=['phase_id','company_id','phase_name','questions']
        # def create(self, validated_data):
        #     questions_data = validated_data.pop('questions')
        #     phase = PA_Phases.objects.create(**validated_data)
        #     for question_data in questions_data:
        #         phases_question.objects.create(phase_id=phase, **question_data)
        #     return phase

class  updatePhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=phases_question
        fields="__all__"
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields="__all__"           

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=choices
        fields="__all__"