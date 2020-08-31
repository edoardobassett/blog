from django.shortcuts import render
from django.views import generic
from blog.models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'blog_index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

