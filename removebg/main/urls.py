from django.urls import path
from . import views

urlpatterns=[
    path('upload',views.upload_pg,name='upload'),
]