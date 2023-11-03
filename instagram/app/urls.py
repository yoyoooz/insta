from django.contrib import admin
from django.urls import path

from app.views.user import CreateUser, LoginUserView, RetrieveUser, UpdateUser, DestroyUser
from app.views.post import CreatePost, RetrievePost, UpdatePost,DestroyPost, RetrieveUserPosts


urlpatterns = [
    path('user/create/', CreateUser.as_view()),
    path('user/login/', LoginUserView.as_view()),
    path('user/<int:pk>/', RetrieveUser.as_view()),
    path('user/update/', UpdateUser.as_view()),
    path('user/delete/<int:pk>', DestroyUser.as_view()),

    path('posts/', RetrieveUserPosts.as_view()),
    path('post/create/', CreatePost.as_view()),
    path('post/<int:pk>/', RetrievePost.as_view()),
    path('post/update/<int:pk>/', UpdatePost.as_view()),
    path('post/delete/<int:pk>/', DestroyPost.as_view()), 

]

