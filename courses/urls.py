
from django.contrib import admin
from django.urls import path
from courses.views import homepage



urlpatterns = [
    path('', homepage.home,name= 'home'),
]
