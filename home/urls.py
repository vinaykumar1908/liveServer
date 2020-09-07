from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    #path('success/', views.homeView, name='TestLink'),
    path('stores/', include('stores.urls')),
    path('ROH/', include('ROH.urls')),
    path('sickline/', include('sickline.urls')),
    path('yard/', include('yard.urls')),
    path('sidings/', include('sidingz.urls')),
    path('MessageBoard/', include('blog.urls')),
    path('MnP/', include('mnp.urls')),
    path('Contracts/', include('contracts.urls')),
    path('Employee/', include('employee.urls')),

    
]
