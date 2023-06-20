from django import template
from blog.models import Blog

register = template.Library()


@register.simple_tag()
def latest_two_blogs():
    return Blog.objects.order_by('-id')[:2]
