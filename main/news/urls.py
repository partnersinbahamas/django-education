
from django.contrib import admin
from django.urls import path, include
from .views import index, by_category

urlpatterns = [
    path('', index, name="news"),
    # <int:pk> means that we will have dynamic link param
    path('category/<int:pk>', by_category, name="category")
]
