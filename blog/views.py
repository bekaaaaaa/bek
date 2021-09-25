from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post

posts = [
    {
        'author': 'Edil',
        'title': 'Omur Bayan',
        'content': 'learning pubg soo easy',
        'post_date': 'September 21, 2021'
    },
    {
        'author': 'Islam',
        'title': 'Love Story',
        'content': 'jealous to Edil',
        'post_date': 'September 15, 2021'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})