from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    # to configure how much and which columns we will se in Article admin
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    # with columns will have a link to the article info
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category')

    # which columns can you edit in Articles list
    list_editable = ('is_published',)

    # which columns can you filter in Articles list
    list_filter = ('created_at', 'updated_at', 'is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields=('name',)

# Register your models here.

admin.site.register(Article, ArticleAdmin) # [model, modelAdmin]
admin.site.register(Category, CategoryAdmin)
