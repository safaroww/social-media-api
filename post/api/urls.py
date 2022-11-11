from django.urls import path
from . import views


urlpatterns = [
    path('post-list/', views.post_list, name='post_list'),
    path('post-list/<int:pk>/', views.post_detail, name='post_detail'),
]
