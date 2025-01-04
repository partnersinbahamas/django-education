from django.shortcuts import render, redirect
from .models import Article
from .templatetags.news_tags import get_all_categories, get_article_by_id
from .form import ArticleForm

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

def view_article(request, article_id):
    article = get_article_by_id(article_id)

    data = {
        'article': article
    }

    return render(request, 'news/article.html', data)

def add_article(request):
    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():
            # in form.cleaned_data saves all fields which passed the validation
            # form.cleaned_data

            # we can use form.save() if our form binded with model used with ModelForm
            article = Article.objects.create(**form.cleaned_data)
            return redirect(article.get_absolute_url())
    else:
        form = ArticleForm()

    data = {
        'form': form,
    }

    return render(request, 'news/add_article.html', data)

