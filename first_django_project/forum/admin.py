from django.contrib import admin
from forum.Models import User, Article, Comment

admin.site.register(User, Article, Comment)
# admin.site.register(Article)
# admin.site.register(Comment)
