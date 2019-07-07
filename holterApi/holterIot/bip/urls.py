from django.urls import path
from . import views

app_name = "bip"

urlpatterns = [
    path('profile', views.ProfilesList.as_view(), name="profile_list"),
    path('profile/<int:pk>/', views.ProfilesDetail.as_view(), name="profile_retrive"),
]
