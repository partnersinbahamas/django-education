from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    # to configure how much and which columns we will se in Article admin
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    # with columns will have a link to the article info
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

# Register your models here.

admin.site.register(Article, ArticleAdmin) # [model, modelAdmin]
