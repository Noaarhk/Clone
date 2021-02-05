from django.contrib import admin
from village.models import Article, Comment, LikeArticle

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeArticle)
