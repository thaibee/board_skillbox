from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='advertisement_list'),
    path('play/', views.play, name='play'),
    path('about/', views.About.as_view(), name='about'),
    path('adver/', views.Adversss.as_view(), name='adver'),
    path('adver2/', views.Adversss.as_view(), name='adver2'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('list/', views.Advertisements.as_view(), name='list'),
    path('list/<int:pk>', views.AdverDetail.as_view(), name='detail'),
]
