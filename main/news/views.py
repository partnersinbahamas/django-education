from django.shortcuts import render
from .models import Article
from .templatetags.news_tags import get_all_categories

# Create your views here.
def index(request):
    news = Article.objects.order_by('-created_at')

    data = {
      'news': news,
    }
    return render(request, 'news/news.html', data)


def by_category(request, pk):
    # pk came from url category/<int:pk> in urls
    news = Article.objects.filter(category_id=pk)
    # using simple tag
    categories = get_all_categories()
    selected_category = categories.get(id=pk)

    data = {
        'news': news,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'news/news.html', data)

