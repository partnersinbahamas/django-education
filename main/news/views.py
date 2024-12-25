from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.

def index(request):
    news = Article.objects.order_by('-created_at')

    data = {
      'news': news,
    }
    return render(request, 'news/news.html', data)

