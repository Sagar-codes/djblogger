from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
# Create your views here.

class HomeView(ListView):
    model = Post
    # template_name = "blog/index.html" # old way to add template files to class based views
    context_object_name = "posts"
    paginate_by = 10

    

    # Sending the template with more data for htmx scroll
    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, 'blog/single.html', {'post':post, 'related':related})