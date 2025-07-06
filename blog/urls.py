from django.urls import path
from . import  views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostdeleteView

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostdeleteView.as_view(),name='post-delete'),
    path('about/', views.about,name='blog-about'),
    
]
