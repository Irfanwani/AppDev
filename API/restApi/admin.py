from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)

# OR another way to register the model is
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')