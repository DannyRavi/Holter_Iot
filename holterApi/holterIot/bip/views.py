from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from json import JSONEncoder
from datetime import datetime
from .serializers import ProfilesSerializer ,UserSerializer, short_Patient_Profiles_Serializer,short_Patient_data_Serializer , all_Patient_data_Serializer

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from .models import Profiles ,patientData
# Create your views here.

class ProfilesList(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class ProfilesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class patientList(generics.ListCreateAPIView):
    queryset = patientData.objects.all()
    serializer_class = all_Patient_data_Serializer

class patientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = patientData.objects.all()
    serializer_class = all_Patient_data_Serializer

#'''kefa'''
class short_Patient_profile_List(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = short_Patient_Profiles_Serializer

class short_Patient_profile_Retrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = short_Patient_Profiles_Serializer


class short_Patient_data_List(generics.ListCreateAPIView):
    queryset = patientData.objects.all()
    serializer_class = short_Patient_data_Serializer

class short_Patient_data_Retrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = patientData.objects.all()
    serializer_class = short_Patient_data_Serializer    
# @csrf_exempt
# @require_POST
# def query_expenses(request):
#     this_token = request.POST['token']
#     num = request.POST.get('num', 10)
#     this_user = get_object_or_404(User, token__token=this_token)
#     expenses = Profiles.objects.filter(user=this_user).order_by('-date')[:num]
#     expenses_serialized = serializers.serialize("json", Profiles)
#     return JsonResponse(expenses_serialized, encoder=JSONEncoder, safe=False)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)