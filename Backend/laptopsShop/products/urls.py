from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view()),
    re_path('^products/(?P<product_id>\d+)/$', views.ProductEditDelete.as_view()),
]