from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SidingHomePageView.as_view(), name='sidings_home' ),
    path('ICD_Okhla/', views.SidingICDOkhlaHomePageView.as_view(), name='siding_ICD_Okhla' ),
    path('sidingModuleRecieved/', views.SidingModuleRecievedPageView.as_view(), name='siding_Modules_Recieved'),
#    path('ACTL/', views.SidingACTLHomePageView.as_view(), name='siding_ACTL' ),
#    path('HTPP/', views.SidingHTPPHomePageView.as_view(), name='siding_HTPP' ),
    path('sidingModuleList/', views.SidingModuleListPageView.as_view(), name='siding_Modules_List'),
    path('sidingModuleList/<int:pk>', views.SidingModuleDetailPageView.as_view(), name='Modules_detail'),
    path('sidingModuleList/<int:pk>/edit/', views.SidingModuleEditView.as_view(), name='Modules_edit'),
    path('sidingModuleList/<int:pk>/editROHDate/', views.SidingModuleEditROHDateView.as_view(), name='Modules_edit_ROHDate'),
    path('sidingModuleList/<int:pk>/editDefect/', views.SidingModuleEditDefectView.as_view(), name='Modules_edit_Defect'),
    path('sidingModuleList/<int:pk>/editDVS/', views.SidingModuleEditDVSView.as_view(), name='Modules_edit_DVS'),
    path('sidingModuleList/<int:pk>/uploadROHFile/', views.SidingModuleEditROHFileView.as_view(), name='Modules_edit_ROHFile'),
    path('moduleName', views.moduleName, name='moduleName'),
    path('ModuleQuickLink', views.ModuleDetailLink, name='ModuleDetailLink'),
    path('RakeQuickLink', views.RakeDetailLink, name='RakeDetailLink'),
    path('DateQuickLink', views.DateDetailLink, name='DateDetailLink'),
    path('DateQuickLinkGZBMUZ', views.DateDetailGZBMUZLink, name='DateDetailGZBMUZLink'),

    path('DateQuickLinkGZBNOLI', views.DateDetailGZBNOLILink, name='DateDetailGZBNOLILink'),

    path('DateQuickLinkPNPBMDJ', views.DateDetailPNPBMDJLink, name='DateDetailPNPBMDJLink'),

    path('DateQuickLinkPNPDWNA', views.DateDetailPNPDWNALink, name='DateDetailPNPDWNALink'),

    path('DateQuickLinkSSBGHH', views.DateDetailSSBGHHLink, name='DateDetailSSBGHHLink'),
    path('DateQuickLinkSSBPTT', views.DateDetailSSBPTTLink,name='DateDetailSSBPTTLink'),
    path('DateQuickLinkTKDACTL', views.DateDetailTKDACTLLink,name='DateDetailTKDACTLLink'),
    path('DateQuickLinkTKDHTPP', views.DateDetailTKDHTPPLink, name='DateDetailTKDHTPPLink'),
    path('DateQuickLinkTKDICD', views.DateDetailTKDICDLink, name='DateDetailTKDICDLink'),
    path('DateQuickLinkYard', views.DateDetailYardLink, name='DateDetailYardLink'),

    path('RakeNumber', views.RakeNumber, name='RakeNumber'),
    path('sidingModuleList/<int:pk>/delete/', views.SidingModuleDeleteView.as_view(), name='Module_delete'),
    path('TKDICDModuleList/', views.TKDICDModuleListPageView, name='TKDICD_Modules_List'),
    path('TKDICDModuleDVSList/', views.TKDICDModuleListDVSPageView, name='TKDICD_Modules_List_DVS'),
    path('TKDHTPPModuleList/', views.TKDHTPPModuleListPageView, name='TKDHTPP_Modules_List'),
    path('TKDHTPPModuleDVSList/', views.TKDHTPPModuleListDVSPageView,name='TKDHTPP_Modules_List_DVS'),
    path('TKDACTLModuleList/', views.TKDACTLModuleListPageView, name='TKDACTL_Modules_List'),
    path('TKDACTLModuleDVSList/', views.TKDACTLModuleListDVSPageView, name='TKDACTL_Modules_List_DVS'),
    path('SSBGHHModuleList/', views.SSBGHHModuleListPageView, name='SSBGHH_Modules_List'),
    path('SSBGHHModuleDVSList/', views.SSBGHHModuleListDVSPageView, name='SSBGHH_Modules_List_DVS'),
    path('SSBPTTModuleList/', views.SSBPTTModuleListPageView, name='SSBPTT_Modules_List'),
    path('SSBPTTModuleDVSList/', views.SSBPTTModuleListDVSPageView, name='SSBPTT_Modules_List_DVS'),

    path('PNPBMDJModuleList/', views.PNPBMDJModuleListPageView, name='PNPBMDJ_Modules_List'),
    path('PNPBMDJModuleDVSList/', views.PNPBMDJModuleListDVSPageView, name='PNPBMDJ_Modules_List_DVS'),

    path('PNPDWNAModuleList/', views.PNPDWNAModuleListPageView, name='PNPDWNA_Modules_List'),
    path('PNPDWNAModuleDVSList/', views.PNPDWNAModuleListDVSPageView, name='PNPDWNA_Modules_List_DVS'),

    path('GZBNOLIModuleList/', views.GZBNOLIModuleListPageView, name='GZBNOLI_Modules_List'),
    path('GZBNOLIModuleDVSList/', views.GZBNOLIModuleListDVSPageView, name='GZBNOLI_Modules_List_DVS'),

    path('GZBMUZModuleList/', views.GZBMUZModuleListPageView, name='GZBMUZ_Modules_List'),
    path('GZBMUZModuleDVSList/', views.GZBMUZModuleListDVSPageView, name='GZBMUZ_Modules_List_DVS'),

    path('YardModuleList/', views.YardModuleListPageView, name='Yard_Modules_List'),
    #path('YardModuleDVSList/', views.YardModuleListDVSPageView, name='Yard_Modules_List_DVS'),


]
