from django.urls import path
from rcb.views import *
app_name='Something'
urlpatterns=[
    path('kingkohli/',kingkohli,name='kingkohli'),
    path('captain/',captain,name='captain'),
]