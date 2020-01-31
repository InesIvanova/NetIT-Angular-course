from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('', views.ProductListView.as_view()),
    # re_path('^(?P<product_id>\d+)/$', views.ProductEditDelete.as_view()),
    path('users/', views.UserListCreate.as_view()),
    re_path('^users/(?P<product_id>\d+)/$', views.UserEditDelete.as_view()),
    path('posts/', views.PostListCreate.as_view()),
    re_path('^posts/(?P<product_id>\d+)/$', views.PostEditDelete.as_view()),
    path('comments/', views.CommentListCreate.as_view()),
    re_path('^comments/(?P<product_id>\d+)/$', views.CommentEditDelete.as_view()),
]