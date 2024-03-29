

from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.JWTTokens import *
from users.JWTTokenAuthentication import JWTAuthentication
from users.permissions import *
from users.backend  import MyAuthentication
from users.models import employers,employer_profile,companies,company_profile
from  users.serializer import companySerializer,employerSerializer,company_profileSerializer, employer_profileSerializer,employer_profileSerializer
from .serializer import (PhaseSerializer, QuestionSerializer, ReviewSerializer, SalarySerializer,updatePhaseSerializer,
ProjectSerializer,LeaveSerializer,DepartmentSerializer,AttendanceSerializer, company_department_serializer,ChoiceSerializer)
from .models import (Attendance, Department_company, Leave, PA_Phases, 
Project,Department,Salary, phases_question,review,choices)

class projects(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[companyPermission]
    def get(self,request,pk=None):
      company_id=request.session['company_id']
      if pk is None:
        try:  
            all_project=Project.objects.filter(company_id=company_id)
            serializer=ProjectSerializer(all_project,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'You have no company'})  
      else:
         try:
          all_project=Project.objects.get(company_id=company_id,project_id=pk)
          serializer=ProjectSerializer(all_project)
          return Response(serializer.data)
         except:
             return Response({'message':'project id is wrong'})

    def post(self,request):
        # request.data['company_id']=request.session['company_id']
        data={
            "title":request.data.get('title'),
            "description":request.data.get('description'),
           "client_name":request.data.get('client_name'),
           "project_leader":request.data.get('project_leader'),
            "start_date":request.data.get('start_date'),
            "end_date":request.data.get('end_date'),
            "status":request.data.get('status'),
            "company_id":request.session['company_id'],
        }
        serializer=ProjectSerializer(data=data)    
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Project added'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    
    def put(self, request,pk=None):
        
        id =pk
        company_id=request.session['company_id']
        project = Project.objects.get(project_id=id,company_id=company_id)
        serializer = ProjectSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Updated'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    def patch(self, request,pk=None):
        id =pk
        company_id=request.session['company_id']
        project = Project.objects.get(project_id=id,company_id=company_id)
        serializer = ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Updated'},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    def delete(self, request, pk, format=None):
        id = pk
        company_id=request.session['company_id']
        project = Project.objects.get(project_id=id,company_id=company_id)
        project.delete()
        return Response({'message':'Project Deleted'},status.HTTP_204_NO_CONTENT)        

class leaves(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[OnlyCompanyPermission]
    def get(self,request,pk=None):
        id=pk
        company_id=request.session['company_id']
        if id is None:
            data=Leave.objects.filter(company_id=company_id)
            serializer=LeaveSerializer(data,many=True)
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            data=Leave.objects.get(leave_id=id,company_id=company_id)
        
            serializer=LeaveSerializer(data)
            return Response(serializer.data,status.HTTP_200_OK)
   
    def patch(self,request,pk=None):
        if pk is not None:
            leave_id=pk
            company_id=request.session['company_id']
            data1=Leave.objects.get(leave_id=leave_id,company_id=company_id)    
            serializer=LeaveSerializer(data1,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'updated'},status.HTTP_201_CREATED)
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) 
        return Response({'message':'leave_id required in params'})      
    def delete(self,request,pk=None): 
        leave_id=pk
        company_id=request.session['company_id']
        leave_obj=Leave.objects.get(leave_id=leave_id,company_id=company_id)    
        leave_obj.delete()
        return Response({'message':'deleted successfully'},status.HTTP_204_NO_CONTENT)

class leave_detail(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[OnlyEmployerPermission]
    def get(self,request):
        emp_id=request.session['emp_id']
        company_id=request.session['company_id']
        data=Leave.objects.filter(emp_id=emp_id,company_id=company_id)
        serializer=LeaveSerializer(data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)      

    def post(self,request):
        data={
            "emp_id":request.session['emp_id'],
            "company_id":request.session['company_id'],
            "subject":request.data.get('subject'),
            "to_date":request.data.get('to_date'),
            "from_date":request.data.get('from_date'),
            "reason":request.data.get('reason'),
            "leave_type":request.data.get('leave_type'),
        }
        serializer=LeaveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'request done'},status.HTTP_201_CREATED)      
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) 
  

class all_departments(APIView):
    authentication_classes=[JWTAuthentication]
   
    def get(self,request):
        all_department=Department.objects.all()
        serializer=DepartmentSerializer(all_department,many=True)
        return Response(serializer.data)   
    def post(self,request):
        data={
            'department_name':request.data.get('department_name'),
            'created_by':request.session['company_id']

        }
        serializer=DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'requested successfully'})  
        return Response(serializer.errors)     

class add_department(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        all_department=Department_company.objects.filter(company_id=request.session['company_id'])
        serializer=company_department_serializer(all_department,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    def post(self,request):
        data={
            "company_id":request.session['company_id'],
            "dept_id":request.data.get('department_id')
        }
        serializer=company_department_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Added'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    
    def delete(self,request,pk=None):
        dept_obj=Department_company.objects.get(id=pk)
        dept_obj.delete()
        return Response({'message':'deleted'},status.HTTP_204_NO_CONTENT)    



class salarys(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[OnlyCompanyPermission]
    def get(self,request,pk=None):
        if pk is not None:
            all_salaries=Salary.objects.filter(emp_id=pk,company_id=request.session['company_id'])
            serializer=SalarySerializer(all_salaries,many=True)
            return Response(serializer.data)
        else:
            all_salaries=Salary.objects.filter(company_id=request.session['company_id'])
            serializer=SalarySerializer(all_salaries,many=True)
            return Response(serializer.data)


    def post(self,request,pk=None):
        company_id=request.session['company_id']
        print(request.data)
        print(pk)
        data={
            "emp_id":pk,
            "company_id":company_id,
            "month":request.data.get('month'),
            "paid_date":request.data.get('paid_date'),
            "salary":request.data.get('salary'),
            
        
        }
        serializer=SalarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'salary paid successfully'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None):
        salary_id=pk
        company_id=request.session['company_id']
        data1=Salary.objects.get(salary_id=salary_id,company_id=company_id)    
        serializer=SalarySerializer(data1,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'updated'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    
    def delete(self,request,pk=None):
        emp_id=pk
        company_id=request.session['company_id']
        data1=Salary.objects.filter(emp_id=emp_id,company_id=company_id)    
        data1.delete()
        return Response({'message':'deleted'},status.HTTP_204_NO_CONTENT)            
class salary_detail(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[OnlyEmployerPermission]
    def get(self,request):      
        all_salaries=Salary.objects.filter(emp_id=request.session['emp_id'],company_id=request.session['company_id'])
        serializer=SalarySerializer(all_salaries,many=True)
        return Response(serializer.data)




class attendance(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[OnlyCompanyPermission]
    def get(self,request):
        data=Attendance.objects.filter(company_id=request.session['company_id'])
        serializer=AttendanceSerializer(data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    def patch(self,request,pk=None):
        attend_obj=Attendance.objects.get(attendance_id=pk,company_id=request.session['company_id'])    
        serializer=AttendanceSerializer(attend_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'updated'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    
    def delete(self,request,pk=None):
         attend_obj=Attendance.objects.get(attendance_id=pk,company_id=request.session['company_id']) 
         attend_obj.delete()
         return Response({'message':'deleted'},status.HTTP_204_NO_CONTENT)
    def post(self,request):
        #request.data['company_id']=request.session['company_id']
        serializer=AttendanceSerializer(data=request.data)# for testing removed many=True
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'saved'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)       
class my_attendance(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[OnlyEmployerPermission]
    def get(self,request):
      
        data=Attendance.objects.filter(emp_id=request.session['emp_id'],company_id=request.session['company_id'])
        serializer=AttendanceSerializer(data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

class check(APIView):
    def post(self,request):
        print(request.data)
        return Response({'message':'done'})          

class salary1(APIView):
     authentication_classes=[JWTAuthentication]
     def post(self,request,pk=None):
         company_id=request.session['company_id']
         print(request.data)
         print(pk)
         data={
             "emp_id":pk,
             "company_id":company_id,
             "month":request.data.get('month'),
             "paid_date":request.data.get('paid_date'),
             "salary":request.data.get('salary'),
             
            
         }
         serializer=SalarySerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return Response({'message':'salary paid successfully'})
         return Response(serializer.errors)
         #return Response({'message':data})
class phaseView(APIView):
     authentication_classes=[JWTAuthentication]
     def get(self,request):
         data=PA_Phases.objects.filter(company_id=request.session['company_id'])
         serializer=PhaseSerializer(data,many=True)
         return Response(serializer.data,status.HTTP_200_OK)
     def post(self,request):
         serializer=PhaseSerializer(data=request.data)  
         if serializer.is_valid():
             serializer.save()
             return Response({'message':'created successfully'},status.HTTP_201_CREATED)
         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)     
     def put(self,request,id=None):
         phase=PA_Phases.objects.get(phase_id=id,company_id=request.session['company_id'])
         serializer=PhaseSerializer(phase,data=request.data)  
         if serializer.is_valid():
             serializer.save()
             return Response({'message':'updated successfully'},status.HTTP_201_CREATED)
         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    
     def patch(self,request,id=None):
         phase=PA_Phases.objects.get(phase_id=id,company_id=request.session['company_id'])
         serializer=PhaseSerializer(phase,data=request.data,partial=True)  
         if serializer.is_valid():
             serializer.save()
             return Response({'message':'partially updated successfully'},status.HTTP_201_CREATED)
         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)     
     def delete(self,request,id=None):
         phase=PA_Phases.objects.get(phase_id=id,company_id=request.session['company_id'])
         phase.delete()
         return Response({'message':'successfully deleted'})           
           
class questionsView(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self,request,id):
        data=PA_Phases.objects.filter(phase_id=id)        
        serializer=PhaseSerializer(data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    def post(self,request):
        if request.data.get('company_id')==request.session['company_id']:
            serializer=QuestionSerializer(data=request.data)  
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'created successfully'},status.HTTP_201_CREATED)
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)     
        return Response(status.HTTP_403_FORBIDDEN)   

    def patch(self,request):
      
     for x in request.data :
      if int(x['company_id'])==request.session['company_id']:
        getdata=phases_question.objects.get(question_id=x['question_id'])
        print(getdata.question_id)
        serializer=updatePhaseSerializer(getdata,data=x,partial=True)
        if serializer.is_valid():
            serializer.save() 
        else:
         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) 
      else:
         return Response({'message':'invalid_company_id or not get company_id'},status.HTTP_403_FORBIDDEN)
     return Response({'message':'updated successfully'},status.HTTP_201_CREATED)
            
     

    def delete(self,request,id=None):
        if request.data.get('company_id')==request.session['company_id']:
            question=phases_question.objects.get(question_id=id)  
            question.delete()
            return Response({'message':'deleted'},status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_403_FORBIDDEN)

class reviewView(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self,request,id=None):
        if id is None:
            data=review.objects.filter(company_id=request.session['company_id'])        
            serializer=ReviewSerializer(data,many=True)
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            data=review.objects.filter(company_id=request.session['company_id'],emp_id=id)        
            serializer=ReviewSerializer(data,many=True)
            return Response(serializer.data,status.HTTP_200_OK)

    def post(self,request,id=None):          
        if request.session['company_id']:
            serializer=ReviewSerializer(data=request.data,many=True)  
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'created successfully'},status.HTTP_201_CREATED)
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)     
        return Response(status.HTTP_403_FORBIDDEN)   

    def patch(self,request):
          for x in request.data :
              getdata=review.objects.get(review_id=x['review_id'],company_id=request.session['company_id'])
              print(getdata)
              serializer=ReviewSerializer(getdata,data=x,partial=True)
              if serializer.is_valid():
                serializer.save()
               
              else:  
               return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)  
          return Response({'message':' successfully updated'})
          



class checkview(APIView):
      def get(self,request,year=None,month=None,week=None,id=None):
            if week=="week1":
                data=review.objects.filter(emp_id=id,weeks__year=year,weeks__month=month,weeks__day="07")        
                serializer=ReviewSerializer(data,many=True)
            if week=="week2":
                data=review.objects.filter(emp_id=id,weeks__year=year,weeks__month=month,weeks__day="14")        
                serializer=ReviewSerializer(data,many=True)    
            if week=="week3":
                data=review.objects.filter(emp_id=id,weeks__year=year,weeks__month=month,weeks__day="21")        
                serializer=ReviewSerializer(data,many=True)
            if week=="week4":
                data=review.objects.filter(emp_id=id,weeks__year=year,weeks__month=month,weeks__day="28")        
                serializer=ReviewSerializer(data,many=True)          
            return Response(serializer.data,status.HTTP_200_OK)

      def patch(self,request,year=None,month=None,week=None,id=None):
          for x in request.data :
              getdata=review.objects.get(review_id=x['review_id'])
              print(getdata)
              serializer=ReviewSerializer(getdata,data=x,partial=True)
              if serializer.is_valid():
                serializer.save()
               
              else:  
               return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)  
          return Response({'message':'done'})
        
class choiceview(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        all_choices=choices.objects.filter(company_id=request.session['company_id'])  
        serializer=ChoiceSerializer(all_choices,many=True) 
        return Response(serializer.data)
    def post(self,request):
        if int(request.data.get('company_id'))==request.session['company_id']:
          serializer=ChoiceSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response({'message':'added successfully'})
          return Response(serializer.errors)
        return Response({'message':'invalid company_id'},status.HTTP_403_FORBIDDEN)     
    def put(self,request,id=None):
        if request.data.get('company_id')==request.session['company_id']:
          choice=choices.objects.get(company_id=request.session['company_id'],choice_id=id) 
          serializer=ChoiceSerializer(choice,data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response({'message':'added successfully'})
          return Response(serializer.errors)
        return Response({'message':'invalid company_id'},status.status.HTTP_403_FORBIDDEN)     

    def delete(self,request,id=None):
        choice=choices.objects.get(company_id=request.session['company_id'],choice_id=id) 
        choice.delete()
        return Response({'message':'deleted'})





