from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home')
]
