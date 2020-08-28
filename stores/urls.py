from django.urls import path
from stores import views

urlpatterns = [
    path('', views.StoresHomePageView.as_view(), name='stores_home' ),
    path('register/', views.RegisterView.as_view(), name='stores_register'),
    path('register/Current/', views.currentStockListView, name='CSR'),
    path('register/Current/new/', views.registerCurrentStockCreateView.as_view(), name='CSR_new'),
    path('register/Current/<int:pk>', views.registerCurrentStockDetailView.as_view(), name='CSR_detail'),
    path('register/Current/<int:pk>/edit/', views.registerCurrentStockEditView.as_view(), name='CSR_edit'),
    path('register/Current/<int:pk>/delete/', views.registerCurrentStockDeleteView.as_view(), name='CSR_delete'),
    path('register/Recieved/', views.registerStockRecievedListView.as_view(), name='SRR'),
    path('register/Recieved/new/', views.registerStockRecievedCreateView.as_view(), name='SRR_new'),
    path('register/Recieved/<int:pk>', views.registerStockRecievedDetailView.as_view(), name='SRR_detail'),
    path('register/Recieved/<int:pk>/edit/', views.registerStockRecievedEditView.as_view(), name='SRR_edit'),
    path('register/Recieved/<int:pk>/delete/', views.registerStockRecievedDeleteView.as_view(), name='SRR_delete'),
    path('register/addNewStock', views.addNewStock, name='addNewStock'),
    path('register/dispatchROH', views.dispatchROH, name='dispatchROH'),
    path('register/dispatchSickline', views.dispatchSickline, name='dispatchSickline'),
    path('register/dispatchYard', views.dispatchYard, name='dispatchYard'),
    path('register/dispatchTrainDuty', views.dispatchTrainDuty, name='dispatchTrainDuty'),
    path('register/dispatchROHregister', views.registerStockDispatchedROH.as_view(), name='SDRR'),
    path('register/dispatchSicklineregister', views.registerStockDispatchSickline.as_view(), name='SDSR'),
    path('register/dispatchYardregister', views.registerStockDispatchedYard.as_view(), name='SDYR'),
    path('register/dispatchTrainDutyregister', views.registerStockDispatchedTrainDuty.as_view(), name='SDTDR'),
    path('ItemAutocomplete', views.autocomplete, name='autocomplete'),
    path('ItemNameAutocomplete', views.ItemNameAutocomplete, name='ItemNameAutocomplete'),
    path('ItemQuickLink', views.ItemQuickLink, name='ItemDetailLink'),
    
]
