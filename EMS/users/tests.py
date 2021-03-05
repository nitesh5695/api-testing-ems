from management.views import attendance
from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import companies,employers
from management.models import Department
from django.urls import reverse
from rest_framework import status
import json
import pdb
 
class Registration(APITestCase):
    def setUp(self) :
        cmp_reg_data={
        "email":"nitesh.singh5695@gmail.com",
        "company_name":"extension",
        "password":"134hgn"
        }
      
        response=self.client.post(reverse('newuser'),cmp_reg_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'],'registered')
        login_data={
        "email":"nitesh.singh5695@gmail.com",
        "password":"134hgn"
        }

        res=self.client.post(reverse('gettoken'),login_data)
        self.token=res.data['access']
      
        self.assertEqual(res.status_code,200)
        
        
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.token)
        data=Department.objects.create(department_name="communication",request="accepted")
        self.assertEqual(data.department_name,'communication')
        emp_data={
        "email":"prince.singh8756@gmail.com",
        "name":"prince",
        "password":"1234hgn"
        }    
        response=self.client.post('/employer_register/',emp_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        res=self.client.get('/employer_register/')
        self.assertEqual(res.status_code,200) 
        res=self.client.post(reverse('gettoken'),emp_data)
        self.emptoken=res.data['access']
        self.assertEqual(res.status_code,200) 
       
        self.project_data={
            "title":"RIPL",
            "description":"ghjgsdf fghsdfgsdhf gsdhgfhjf gfjhdgfhsdf jhdfhdfui  fgsdfhsfgj ",
           "client_name":"smilebot",
           "project_leader":"nitesh",
            "start_date":"2021-03-21",
            "end_date":"2021-08-21",
            "status":"On Hold",
            "company_id":"1",   # this field is only used in patch,put operations
            
            
        }     
        res=self.client.post(reverse('projects'),self.project_data) 
        
        self.assertEqual(res.status_code,201)
    def test_companyProfile(self):
        data={
            "company_id":1,
            "ceo":"nitesh",
            "established_year":2008,
            "address":"gorakhpur",
            "contact_no":8874411916,
            "gst_no":"gstin45657"
        }
      
        response=self.client.post(reverse('company_profile'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response=self.client.put(reverse('company_profile'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response=self.client.patch(reverse('company_profile'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response=response=self.client.delete(reverse('company_profile'))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_project(self):
        self.project_data={
            "title":"RIPL",
            "description":"ghjgsdf fghsdfgsdhf gsdhgfhjf gfjhdgfhsdf jhdfhdfui  fgsdfhsfgj ",
           "client_name":"smilebot",
           "project_leader":"nitesh",
            "start_date":"2021-03-21",
            "end_date":"2021-08-21",
            "status":"On Hold",
            "company_id":"1",   # this field is only used in patch,put operations
            
            
        }  
        
        res=self.client.put(reverse('projects_id',args=[1]), self.project_data) 
        self.assertEqual(res.status_code,201)
        res=self.client.patch(reverse('projects_id',args=[1]), self.project_data) 
        self.assertEqual(res.status_code,201)
        res=self.client.get(reverse('projects')) 
        self.assertEqual(res.status_code,200)
        res=self.client.delete(reverse('projects_id',args=[1])) 
        self.assertEqual(res.status_code,204)

    def test_EDepartment_by_company(self):
        data={
            "company_id":1,
            "department_id":1,
        }   
        res=self.client.post(reverse('add_department'),data) 
        self.assertEqual(res.status_code,201)
        res=self.client.get(reverse('projects')) 
        self.assertEqual(res.status_code,200)
        res=self.client.delete(reverse('add_department_id',args=[1])) 
        self.assertEqual(res.status_code,204)

    def test_employer_profile(self):
         data={
             "emp_id":1,
             "gender":"Male",
             "job_type":"Full Time",
             "address":"faridabad",
             "mobile_no":8874411916,
             "dob":"1998-06-05",
             "joining_date":"2021-02-01",
             "project_id":1,
             "department_id":1,
             "status":"Active",
         }   
         response=self.client.post(reverse('employer_profile'),data)
         self.assertEqual(response.status_code,201)
         response=self.client.patch(reverse('employer_profile_id',args=[1]),data)
         self.assertEqual(response.status_code,201)
         response=self.client.delete(reverse('employer_profile_id',args=[1]),data)
         self.assertEqual(response.status_code,204)

    def test_salary(self):
        salary_data={
            "month":"January",
             "paid_date": "2021-05-01",
             "salary": 20000,
            "description": " jfdf gfhgfd jhgfhjdf  dgfjhd",
        }
        res=self.client.post(reverse('salary_empid',args=[1]),salary_data)
        self.assertEqual(res.status_code,201)
        res=self.client.get(reverse('salary_empid',args=[1]))
        self.assertEqual(res.status_code,200)
        res=self.client.get(reverse('salary'))
        self.assertEqual(res.status_code,200)
        res=self.client.patch(reverse('salary_empid',args=[1]),salary_data)
        self.assertEqual(res.status_code,201)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.emptoken)
        res=self.client.get(reverse('employer_salary'))
        self.assertEqual(res.status_code,200)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.token)
        res=self.client.delete(reverse('salary_empid',args=[1]))
        self.assertEqual(res.status_code,204)
    
    def test_leave(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.emptoken)
        leave_data={
            "subject":"urgent work",
        "from_date":"2021-05-3",
        "to_date":"2021-05-05",
        "leave_type":"Special",
        "reason":"fever vvbb vxvbmvbx vcxvbxmv bvxbviue jhwhzm jh  j bzzxc jhjhjkdz czhcjk"

        }    
        res=self.client.post(reverse('apply_leave'),leave_data)
        self.assertEqual(res.status_code,201)
        res=self.client.get(reverse('apply_leave'))
        self.assertEqual(res.status_code,200)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.token)
        res=self.client.get(reverse('manage_leaves'))
        self.assertEqual(res.status_code,200)
        res=self.client.get(reverse('manage_leaves_id',args=[1]))
        self.assertEqual(res.status_code,200)
        res=self.client.patch(reverse('manage_leaves_id',args=[1]))
        self.assertEqual(res.status_code,201)
        res=self.client.delete(reverse('manage_leaves_id',args=[1]))
        self.assertEqual(res.status_code,204)

    def test_attendance(self):
     attendance_data= {
                "company_id":"1",
                "emp_id":1,
                "status":"Present",
                "date":"2021-05-03"
            }
    
     res=self.client.post(reverse('attendance'),attendance_data)
     self.assertEqual(res.status_code,201)
     res=self.client.get(reverse('attendance'))
     self.assertEqual(res.status_code,200)
     res=self.client.patch(reverse('attendance_id',args=[1]),attendance_data)
     self.assertEqual(res.status_code,201)
     res=self.client.delete(reverse('attendance_id',args=[1])) 
     self.assertEqual(res.status_code,204)

     self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.emptoken)
     res=self.client.get(reverse('my_attendance'))
     self.assertEqual(res.status_code,200)

    def test_search(self):
        res=self.client.get(reverse('search_employer',args=['pri'])) 
        self.assertEqual(res.status_code,200)
    def test_dashboard(self):
        res=self.client.get(reverse('company_dashboard')) 
        self.assertEqual(res.status_code,200)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.emptoken)
        res=self.client.get(reverse('employer_dashboard')) 
        self.assertEqual(res.status_code,200)
    def test_forget_password(self):
        data={
            "email":"nitesh.singh5695@gmail.com"
        }    
        res=self.client.post(reverse('forget_password'),data)
        self.assertEqual(res.status_code,202)
        otp={
           "otp":"1234"
        }
        res=self.client.post(reverse('otp_verification'),otp)
        self.assertEqual(res.status_code,202)
        new_pass={
            "new_password":"nitesh",
            "confirm_password":"nitesh"
        }
        res=self.client.patch(reverse('otp_verification'),new_pass)
        self.assertEqual(res.status_code,202)










  






