from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    content = models.TextField()
    like = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=10)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f"Comment on '{self.parent_post}' by {self.author}"