from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, UserPostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/new/', views.newcomment, name='new-comment'),
    path('post/<int:pk>/comments/', views.comments, name='comments'),
    path('about/', views.about, name='blog-about'),
   	]

