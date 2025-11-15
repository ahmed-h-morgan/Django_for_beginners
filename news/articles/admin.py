from django.contrib import admin

from .models import Article, Comment     # NEW

# Register your models here.

class CommentInline(admin.StackedInline): # new - use StackedInline to display the mouuels relations in admin page
    model = Comment
    extra = 0 # new  - update the value of this attribute from 3 (the default value) to 0


# class CommentInline(admin.TabularInline): # new  - use TabularInline to display the mouuels relations in admin page
#     model = Comment

class ArticleAdmin(admin.ModelAdmin): # new 
    inlines = [ CommentInline, ]


admin.site.register(Article, ArticleAdmin)      # NEW - register articles to admin
admin.site.register(Comment) # new - register comment - model to admin to make it visible into the admin page
