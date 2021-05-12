from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='user_posts')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, 
                            on_delete=models.CASCADE, 
                            related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE, 
                            related_name='user_likes')
    updated = models.DateTimeField(auto_now=True)
