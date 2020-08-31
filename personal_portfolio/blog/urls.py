from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_detail'),
    path("<category>/", views.blog_category, name="blog_category"),
]