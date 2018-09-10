from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Hello World')


def post_list(request):
    return render(request, 'blog/post_list.html', {})