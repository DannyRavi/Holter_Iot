from rest_framework import serializers
from .models import Profiles ,patientData
import re
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    snippetz = serializers.PrimaryKeyRelatedField(many=True, queryset=Profiles.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')


class short_Patient_Profiles_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('user', 'first_name','last_name','nation_code','emergency_request')


class all_Patient_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = patientData
        fields = "__all__"


class short_Patient_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = patientData
        fields = ('user', 'indications','medications','technicain_name','emergency_status','hospitalization')