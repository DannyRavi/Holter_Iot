from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from json import JSONEncoder
from datetime import datetime
from .serializers import ProfilesSerializer

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_POST


from .models import Profiles ,patientData
# Create your views here.

class ProfilesList(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class ProfilesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
