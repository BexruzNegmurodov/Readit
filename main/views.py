from django.shortcuts import render
from blog.models import Blog, SubBlog, Tag, Category
from django.core.paginator import Paginator
from .models import Feedback


def home(request):
    objects = Blog.objects.order_by('-id')
    paginator = Paginator(objects, 1)  # Show 25 contacts per page
    page = request.GET.get('page', 1)
    object_list = paginator.get_page(page)
    ctx = {
        'obj': object_list,
        'blogs': objects[:2]
    }
    return render(request, 'main/index.html', ctx)


def about(request):
    feeds = Feedback.objects.all
    ctx = {
        'feeds': feeds
    }
    return render(request, 'main/about.html', ctx)
