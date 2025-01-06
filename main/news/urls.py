from django.urls import path
from .views import view_article, add_article, HomeNewsList, NewsByCategory

urlpatterns = [
    path('', HomeNewsList.as_view(), name="news"),
    # in NewsByCategory.as_view() we can add extra_context in view params
    path('category/<int:pk>', NewsByCategory.as_view(extra_context={'page_name': 'category'}), name="category"),
    # <int:pk> means that we will have dynamic link param
    path('news/<int:article_id>', view_article, name="view_article"),
    path('news/add-article', add_article, name="add_article")
]