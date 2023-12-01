from django.urls import path
from .views import *

urlpatterns = [
    path('user/signup/', signup, name='signup'),
    path('user/login/', login, name='login'),
    path('post/create/', create_post, name='create_post'),
    path('user/like_post/', like_post, name='like_post'),
    path('user/comment_post/', comment_post, name='comment_post'),
    path('user/follow/', follow, name='follow'),
    path('user/following/', following, name='following'),
    path('user/followers/', followers, name='followers'),
    path('user/posts/', posts, name='posts'),
    path('post/all_posts/', all_posts, name='all_posts'),
    path('post/edit/<int:id>', edit_post, name='edit_post'),
    path('post/delete/<int:id>/', delete_post, name='delete_post'),
    path('post/view/<int:id>/', view_post, name='view_post'),
    path('user/unfollow/', unfollow, name='unfollow'),
    path('user/like_post/<int:post_id>/', like_post, name='unlike_post'),
    path('user/unlike_post/<int:post_id>/', unlike_post, name='unlike_post'),
    path('user/logout/', logout, name='logout'),
]