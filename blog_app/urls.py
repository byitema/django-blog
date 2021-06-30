from .views import PostDetail, PostList
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail')
]
