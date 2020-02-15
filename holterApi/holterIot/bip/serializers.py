from rest_framework import serializers
from .models import Profiles 
import re
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.ModelSerializer):
    snippetz = serializers.PrimaryKeyRelatedField(many=True, queryset=Profiles.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')

class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = "__all__"

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('user','id', 'first_name','last_name','nation_code','emergency_request','emergency_status','hospitalization')



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('user','id','first_name','last_name','phone_number','mobile_number','age','group','nation_code','height','weigth ','address','postal_code','email','gender')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields =  ('user','id','emergency_request','emergency_status','hospitalization','angina','history_of_mi','prior_cath','prior_cabg','smoking','diabetic','family_history','paec_maker','indications','medications','procedure_type','referring_physician','notes','technicain_name','attending_phy','request_time_data', 'location')
