from django.urls import path
from main.views import *


app_name = "product"

urlpatterns = [
    path("", main, name='main')
]
