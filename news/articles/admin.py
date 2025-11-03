from django.contrib import admin

from .models import Article     # NEW

# Register your models here.

admin.site.register(Article)      # NEW - register articles to admin