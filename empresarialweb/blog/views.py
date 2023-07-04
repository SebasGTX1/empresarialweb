from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", context={'posts': posts})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", context={'category': category, 'posts': posts})
