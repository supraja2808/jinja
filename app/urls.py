from django.urls import path
from app.views import *

urlpatterns=[
    path('jinja/',jinja,name='jinja'),
]