from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.


def home(request):
    return HttpResponse('Hello World')


def post_list(request):
    posts = Post.objects.all().order_by(
        'published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})