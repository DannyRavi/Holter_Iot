from django.urls import path
from . import views
from .views import login, sample_api

app_name = "bip"

urlpatterns = [
    path('profile/', views.ProfilesList.as_view(), name="profile_list"),
    path('profile/<int:pk>/', views.ProfilesDetail.as_view(), name="profile_retrive"),
    path('profile/short/', views.short_Patient_profile_List.as_view(), name="profile_short_list"),
    path('profile/short/<int:pk>/', views.short_Patient_profile_Retrieve.as_view(), name="profile_short_retrive"),
    path('patient/', views.patientList.as_view(), name="patient_list"),
    path('patient/<int:pk>/', views.patientDetail.as_view(), name="patient_retrive"),
    path('patient/short/', views.short_Patient_data_List.as_view(), name="profile_short_list"),
    path('patient/short/<int:pk>/', views.short_Patient_data_Retrieve.as_view(), name="profile_short_retrive"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api/login', login),
    path('api/sampleapi', sample_api),
]
