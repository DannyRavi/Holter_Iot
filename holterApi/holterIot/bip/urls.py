from django.urls import path
from . import views
from .views import login, sample_api

app_name = "bip"

urlpatterns = [
    path('All/', views.allDataList.as_view(), name="All_list"),
    path('All/<int:pk>/', views.allDataDetail.as_view(), name="All_retrive"),
    path('profile/', views.profilesList.as_view(), name="profiles_list"),
    path('profile/<int:pk>/', views.profilesDetail.as_view(), name="profile_Detail"),
    path('emergency/', views.emergencyList.as_view(), name="emergency_list"),
    path('emergency/<int:pk>/', views.emergencyDetail.as_view(), name="emergency_retrive"),
    path('patient/', views.patientList.as_view(), name="patient_list"),
    path('patient/<int:pk>/', views.patientDetail.as_view(), name="patient_retrive"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api/login', login),
    path('api/sampleapi', sample_api),
]


