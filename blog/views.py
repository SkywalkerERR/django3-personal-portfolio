from django.shortcuts import render, get_object_or_404
from .models import Blogs


def all_blogs(request):
    allblogs = Blogs.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'allblogs' : allblogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id) # Функция пытается найти объект под нужным номером в БД
    return render(request, 'blog/detail.html', {'blog' : blog})