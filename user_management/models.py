from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.post.name


class TP(models.Model):
    name = models.CharField(max_length=30, default=None)
