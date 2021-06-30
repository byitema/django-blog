from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-creation_date')
    template_name = 'post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
