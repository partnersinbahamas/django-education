
from django.contrib import admin
from django.urls import path, include
from .views import by_category, view_article, add_article, HomeNewsList

urlpatterns = [
    path('', HomeNewsList.as_view(), name="news"),
    # <int:pk> means that we will have dynamic link param
    path('category/<int:pk>', by_category, name="category"),
    path('news/<int:article_id>', view_article, name="view_article"),
    path('news/add-article', add_article, name="add_article")
]