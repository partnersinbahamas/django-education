
from django.contrib import admin
from django.urls import path, include
from .views import index, by_category, view_article

urlpatterns = [
    path('', index, name="news"),
    # <int:pk> means that we will have dynamic link param
    path('category/<int:pk>', by_category, name="category"),
    path('news/<int:article_id>', view_article, name="view_article")
]
