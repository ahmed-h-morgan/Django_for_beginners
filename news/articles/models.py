# articles/models.py
from django.db import models
from django.urls import reverse
from django.conf import settings     # to be able to use the customized user_model by settings.AUTH_USER_MODEL as below



# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,    # use settings.AUTH_USER_MODEL to create a forign key to a primary key in the customized user model
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})

class Comment(models.Model): # new
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")