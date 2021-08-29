from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('delete/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
]