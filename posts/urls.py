from django.urls import path
from .views import *

app_name='posts'

urlpatterns = [
    path('', post_list), #localhost:8000/posts
    path('/create', post_create), #localhost:8000/posts/create
    path('/<int:pk>', post_detail), 
    path('/<int:pk>/update', post_update),
    path('/<int:pk>/delete', post_delete),
    path('/<int:pk>/comments/create', comment_create),
]

