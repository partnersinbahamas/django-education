from django.contrib import admin
from .models import Article, Category
from django.utils.safestring import mark_safe


class ArticleAdmin(admin.ModelAdmin):
    # to configure how much and which columns we will se in Article admin
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'render_image')
    # with columns will have a link to the article info
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category')
    # fields which we will see in admin Article detail
    fields = ('id', 'title', 'content', 'is_published', 'category', 'image', 'render_image', 'views', 'created_at', 'updated_at')
    # non-editable field
    readonly_fields = ('id', 'views', 'created_at', 'updated_at', 'render_image')

    # add save button on save of admin change forms
    save_on_top = True

    # which columns can you edit in Articles list
    list_editable = ('is_published',)

    # which columns can you filter in Articles list
    list_filter = ('created_at', 'updated_at', 'is_published', 'category')

    # to render image in admin as html tag
    def render_image(self, obj):
        if obj.image:
            # mark_safe makes our image not as 'escaped'
            return mark_safe(f'<img src="{obj.image.url}" width="40" height="40">')
    
    # to see right name in admin instead of 'render image'
    render_image.short_description = "Image"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields=('name',)

# Register your models here.

admin.site.register(Article, ArticleAdmin) # [model, modelAdmin]
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Administation panel'
admin.site.site_header = 'Web aministation'
admin.site.subtitle = ''
