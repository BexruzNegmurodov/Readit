from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

from profiles.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=201)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=201)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=201)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=201)
    prepopulated_fields = {'slug': ('title',)}
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blogs')
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    @property
    def full_url(self):
        url = reverse('blog:blog_single', kwargs={
            'year': self.created_date.year,
            'month': self.created_date.month,
            'day': self.created_date.day,
            'slug': self.slug
        })
        return url

    @property
    def counter_view(self):
        self.views += 1
        return self.views


# class BlogTag(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class SubBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=201)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.blog.title


def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        print(instance.slug)


pre_save.connect(blog_pre_save, sender=Blog)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=221)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    question = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
