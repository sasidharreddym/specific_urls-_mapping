from django.urls import path
from p6a2.views import *

app_name='IRONMAN'

urlpatterns=[
    path('ironman/',ironman,name='ironman'),
    path('rhodes/',rhodes,name='rhodes'),

]