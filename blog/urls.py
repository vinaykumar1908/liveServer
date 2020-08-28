from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blogHome'),
    #path('success/', views.homeView, name='TestLink'),

]



