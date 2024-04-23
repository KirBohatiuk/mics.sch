from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post


def homepage(request):
    return render(request, 'MicsApp/homepage.html')


def blog(request):
    posts = Post.objects.order_by('-creation_date')[:2]
    return render(request, 'MicsApp/blog.html', {'posts': posts})


def assign_lesson(request):
    return render(request, 'MicsApp/assign_lesson.html')


def contact_info(request):
    return render(request, 'MicsApp/contact_info.html')
