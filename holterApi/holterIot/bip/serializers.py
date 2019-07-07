from rest_framework import serializers
from .models import Profiles ,patientData
import re
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('id', 'user', 'nation_code', 'first_name', 'last_name', 'age')


