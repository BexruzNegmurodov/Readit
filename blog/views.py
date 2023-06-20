from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages

from profiles.models import Profile
from main.models import Feedback
from .forms import BlogForm
from .models import Blog, SubBlog, Tag, Category, Comment


def articles(request):
    objects = Blog.objects.order_by('-id')
    q = request.GET.get('q')
    category_q = request.GET.get('category_q')
    tag_q = request.GET.get('tag_q')
    if q:
        objects = objects.filter(title__icontains=q)
    if category_q:
        objects = objects.filter(category__title__exact=category_q)
    if tag_q:
        objects = objects.filter(tags__title__exact=tag_q)
    paginator = Paginator(objects, 2)
    page = request.GET.get('page')
    obj = paginator.get_page(page)

    ctx = {
        'obj': obj,

    }
    return render(request, 'blog/blog.html', ctx)


def blog_single(request, **kwargs):
    slug = kwargs.get('slug')
    year = kwargs.get('year')
    month = kwargs.get('month')
    day = kwargs.get('day')
    obj = get_object_or_404(Blog, created_date__year=year, created_date__month=month, created_date__day=day, slug=slug)
    obj.views += 1
    obj.save()
    print(obj.views)
    prof = Profile.objects.get(user_id=obj.author.id)
    category = Category.objects.all()
    tags = Tag.objects.all()
    latest_blogs = Blog.objects.order_by('-id')[:3]

    ctx = {
        'obj': obj,
        'prof': prof,
        'category': category,
        'tags': tags,
        'latest_blogs': latest_blogs,



    }
    return render(request, 'blog/blog-single.html', ctx)


def comment(request, **kwargs):

    # obj = Blog.objects.get(slug=kwargs.get('slug'))
    # print(obj.title)
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been accepted')
            # return redirect(reverse('blog:blog_single', kwargs={'pk': blog_id}))
    ctx = {
        'form': form,
    }
    return render(request, 'blog/comment.html', ctx)
