from django.contrib import admin
from .models import Article, Comment,BlockList


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass



@admin.register(BlockList)
class BlockListAdmin(admin.ModelAdmin):
    pass
