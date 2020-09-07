from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='cblogHome'),
    path('cuser/<str:username>', UserPostListView.as_view(), name='cuser-posts'),
    path('cpost/<int:pk>/', PostDetailView.as_view(), name='cpost-detail'),
    path('cpost/new/', PostCreateView.as_view(), name='cpost-create'),
    path('cpost/<int:pk>/update/', PostUpdateView.as_view(), name='cpost-update'),
    path('cpost/<int:pk>/delete/', PostDeleteView.as_view(), name='cpost-delete'),
    #path('success/', views.homeView, name='TestLink'),
    path('cpost/<int:pk>/comment/', views.add_comment_to_post,name='cadd_comment_to_post'),
    #path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('ccomment/<int:pk>/remove/', views.comment_remove, name='ccomment_remove'),

]
