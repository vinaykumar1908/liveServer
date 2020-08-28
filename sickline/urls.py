from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SicklineHomePageView.as_view(), name='sickline_home' ),
    path('SicklineModules', views.SicklineModules, name='Sickline_Modules'),
]
