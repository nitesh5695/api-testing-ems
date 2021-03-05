
from .models import companies,employers
from rest_framework import exceptions
class MyAuthentication():
    def login(request,username):
        request.session['username']=username
        return True
    def isemployee(email):
        try:
            user=employers.objects.get(email=email) 
            return True
        except employers.DoesNotExist:
            return False    
    def iscompany(email):
        try:
            user=companies.objects.get(email=email) 
            return True
        except companies.DoesNotExist:
            return False            

    def authenticate(request,email=None, password=None):    
        try:
            user= employers.objects.get(email=email,password=password)
            return user
        except employers.DoesNotExist:
            try:
                print(" company")
                user=companies.objects.get(email=email,password=password)
                
                return user
            except:
                raise exceptions.AuthenticationFailed('email or password is wrong')    
            
           
           
        except companies.DoesNotExist:
            print("not exist")
            return None
        except Exception as e:
            print("not exist1")
            
            return None

        
            