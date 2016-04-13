from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def post_list(request):

    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogtests.html", {'posts': post})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1 #clock up the number of times the post has been viewed
    post.save()
    return render(request, "blogdetail.html", {'post': post})

def post_top5(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:2]
    return render(request, "blogtests.html", {'posts': post})

def new_post(request):
    form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})