from django.urls import path
from p6a1.views import *


app_name='AVENGERS'


urlpatterns=[
    path('captainamerica/',captainamerica,name='captainamerica'),
    path('thor/',thor,name='thor'),

]