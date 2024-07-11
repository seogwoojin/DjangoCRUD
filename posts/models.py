from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=40)
    user=models.CharField(max_length=20)
    content=models.TextField()
    

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()