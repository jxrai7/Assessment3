from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widget/', views.widget_index, name='index'),
    # path('posts/', posts.as_view(), name='posts_index'),
]