from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name='index'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("check_username/", check_username, name='check_username'),
    path("check_subject/", check_subject, name='check_subject'),
    path("check_dob/", check_dob, name='check_dob'),
]