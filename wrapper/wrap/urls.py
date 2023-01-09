from django.urls import path
from . import views

app_name = 'wrap'

urlpatterns = [
    path('', views.index, name="index")
]