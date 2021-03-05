from django.db.models import fields
from rest_framework import serializers
from .models import employers,employer_profile,companies,company_profile


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model=companies
        fields="__all__"
        extra_kwargs = {
           
            'password': {'write_only': True}
        }

class employerSerializer(serializers.ModelSerializer):
    class Meta:
        model=employers
        fields="__all__"     
        extra_kwargs = {
           
            'password': {'write_only': True}
        }   
    
class company_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=company_profile
        fields="__all__"

class employer_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=employer_profile
        fields="__all__"         


