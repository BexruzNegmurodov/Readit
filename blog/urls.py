from django.urls import path
from .views import articles, blog_single, comment

app_name = 'blog'

urlpatterns = [
    path('article/', articles, name='articles'),
    path('blog_single/<str:year>/<str:month>/<int:day>/<slug:slug>', blog_single, name='blog_single'),
    path('blog-single/comment', comment, name='comment')
]
