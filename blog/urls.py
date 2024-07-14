from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>',views.CategoryView.as_view(),name='category'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
    path('comment/<int:post_pk>',views.CommentView.as_view(),name='comment'),
    
]