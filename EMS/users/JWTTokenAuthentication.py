from requests.models import DecodeError
from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication
from .models import companies,employers
from rest_framework import exceptions
import jwt
from django.conf import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_data=authentication.get_authorization_header(request)
        if not auth_data:
            raise exceptions.AuthenticationFailed('please provide token')
        try:  
          prefix,token =auth_data.decode('utf-8').split(' ')
          
          if prefix != "Bearer":
            raise exceptions.AuthenticationFailed('invalid token prefix')

        except DecodeError:
           raise exceptions.AuthenticationFailed('please provide token with prefix')
        try:
        
          payload=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
          
          email=payload['username']
          print(payload)
          user =employers.objects.get(email=email)
          request.session['emp_id']=user.emp_id
          request.session['username']=user.email
                 
          request.session['company_id']=user.company_id.company_id
         
          #print(request.user)
         # print(user)
          return (user,token)
        except employers.DoesNotExist:
          payload=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
          print(payload)
          email=payload['username']
         
          user =companies.objects.get(email=email)

          request.session['company_id']=user.company_id
          request.session['username']=user.email
          print("register user")
          return (user,token)  
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('your token is invalid')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('token is expired')