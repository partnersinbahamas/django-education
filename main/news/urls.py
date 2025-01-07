from django.urls import path
from .views import add_article, HomeNewsList, NewsByCategory, ArticleView

urlpatterns = [
    path('', HomeNewsList.as_view(), name="news"),
    # in NewsByCategory.as_view() we can add extra_context in view params
    # <int:pk> means that we will have dynamic link param
    path('category/<int:pk>', NewsByCategory.as_view(extra_context={'page_name': 'category'}), name="category"),
    path('news/<int:article_id>', ArticleView.as_view(), name="view_article"),
    path('news/add-article', add_article, name="add_article")
]