from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.YardHomePageView.as_view(), name='yard_home' ),
    
]
