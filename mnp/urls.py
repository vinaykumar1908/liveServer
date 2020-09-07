from django.urls import path, include
from .views import mnpPostListView, mnpPostDetailView, mnpPostCreateView, mnpPostUpdateView, mnpPostDeleteView, mnpUserPostListView
from . import views

urlpatterns = [
    path('', mnpPostListView.as_view(), name='mnpHome'),
    path('user/<str:username>', mnpUserPostListView.as_view(), name='mnpuser-posts'),
    path('mnppost/<int:pk>/', mnpPostDetailView.as_view(), name='mnppost-detail'),
    path('mnppost/new/', mnpPostCreateView.as_view(), name='mnppost-create'),
    path('mnppost/<int:pk>/update/', mnpPostUpdateView.as_view(), name='mnppost-update'),
    path('mnppost/<int:pk>/delete/', mnpPostDeleteView.as_view(), name='mnppost-delete'),
    #path('success/', views.homeView, name='TestLink'),
    path('mnppost/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
    #path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='pcomment_remove'),


]
