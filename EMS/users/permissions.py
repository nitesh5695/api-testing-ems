from rest_framework.permissions import BasePermission
from .backend  import MyAuthentication
from  .models  import companies,employers
class companyPermission(BasePermission):
    
    def has_permission(self, request, view):
      email=request.session['username']
      is_employee=MyAuthentication.isemployee(email)
      if(is_employee):
          if request.method=='GET':
              return True
          else:
              return False 
      else:
          return True

class employerPermission(BasePermission):
    def has_permission(self, request, view):
        
        email=request.session['username']
        is_employee=MyAuthentication.isemployee(email)
        if(is_employee):
            if request.method=='GET' or request.method=='POST':
                return True
            else:
                return False 
        elif request.method=='GET' or request.method=='PATCH' or request.method=='DELETE':
            return True
        else:
            return False    
       

class OnlyEmployerPermission(BasePermission):
     
    def has_permission(self, request, view):
      email=request.session['username']
      is_employee=MyAuthentication.isemployee(email)
      if(is_employee):
              return True
      else:
              return False 

class OnlyCompanyPermission(BasePermission):
     
    def has_permission(self, request, view):
      email=request.session['username']
      is_employee=MyAuthentication.isemployee(email)
      if(is_employee):
              return False
      else:
              return True       