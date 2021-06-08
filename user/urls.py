from django.urls import path
from .views import *

urlpatterns = [
    path('', auth),
    path('auth2/', Auth2.as_view(), name='auth2')
]
