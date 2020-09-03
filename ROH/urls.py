from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='ROH_home' ),
    path('register/', views.RegisterView.as_view(), name='ROH_Register' ),
    path('register/WRJudwR/', views.registerWheelRecievedJudwListView.as_view(), name='WRJudwR'),
    path('register/WRJudwR/new/', views.registerWheelRecievedJudwCreateView.as_view(), name='WRJudwR_new'),
    path('register/WRJudwR/<int:pk>', views.registerWheelRecievedJudwDetailView.as_view(), name='WRJudwR_detail'),
    path('register/WRJudwR/<int:pk>/edit/', views.registerWheelRecievedJudwEditView.as_view(), name='WRJudwR_edit'),
    path('register/WRJudwR/<int:pk>/delete/', views.registerWheelRecievedJudwDeleteView.as_view(), name='WRJudwR_delete'),
    path('register/WDJudwR/', views.registerWheelDispatchedJudwListView.as_view(), name='WDJudwR'),
    path('register/WDJudwR/new/', views.registerWheelDispatchedJudwCreateView.as_view(), name='WDJudwR_new'),
    path('register/WDJudwR/<int:pk>', views.registerWheelDispatchedJudwDetailView.as_view(), name='WDJudwR_detail'),
    path('register/WDJudwR/<int:pk>/edit/', views.registerWheelDispatchedJudwEditView.as_view(), name='WDJudwR_edit'),
    path('register/WDJudwR/<int:pk>/delete/', views.registerWheelDispatchedJudwDeleteView.as_view(), name='WDJudwR_delete'),
    path('register/HAWR/', views.registerHotAxleWagonListView.as_view(), name='HAWR'),
    path('register/HAWR/new/', views.registerHotAxleWagonCreateView.as_view(), name='HAWR_new'),
    path('register/HAWR/<int:pk>', views.registerHotAxleWagonDetailView.as_view(), name='HAWR_detail'),
    path('register/HAWR/<int:pk>/edit/', views.registerHotAxleWagonEditView.as_view(), name='HAWR_edit'),
    path('register/HAWR/<int:pk>/delete/', views.registerHotAxleWagonDeleteView.as_view(), name='HAWR_delete'),
    path('register/GC/', views.registerGaugeCalibrationListView.as_view(), name='GC'),
    path('register/GC/new/', views.registerGaugeCalibrationCreateView.as_view(), name='GC_new'),
    path('register/GC/<int:pk>', views.registerGaugeCalibrationDetailView.as_view(), name='GC_detail'),
    path('register/GC/<int:pk>/edit/', views.registerGaugeCalibrationEditView.as_view(), name='GC_edit'),
    path('register/GC/<int:pk>/delete/', views.registerGaugeCalibrationDeleteView.as_view(), name='GC_delete'),
    path('ROHModules', views.ROHModules, name='ROH_Modules'),
    path('ROHModulesFIT', views.ROHModulesFIT, name='ROH_Modules_FIT'),

]


