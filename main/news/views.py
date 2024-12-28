from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category


# Create your views here.

def index(request):
    news = Article.objects.order_by('-created_at')
    categories = Category.objects.all()

    data = {
      'news': news,
      'categories': categories,
    }
    return render(request, 'news/news.html', data)


def by_category(request, pk):
    # pk came from url category/<int:pk> in urls
    news = Article.objects.filter(category_id=pk)
    categories = Category.objects.all()
    selected_category = categories.get(id=pk)

    data = {
        'news': news,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'news/news.html', data)

