from django.contrib import admin
from .models import Tag, Category, Blog, SubBlog, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class SubBlogInline(admin.StackedInline):
    model = SubBlog
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (SubBlogInline,)
    list_display = ('id', 'author', 'title', 'slug', 'category', 'created_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author__username', 'category__title')
    filter_horizontal = ('tags',)
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'


@admin.register(SubBlog)
class SubBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'title')
    search_fields = ('blog__title', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'full_name', 'question')
    search_fields = ('blog', 'full_name')
