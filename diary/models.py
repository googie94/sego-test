from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=20)
    post = models.ForeignKey('diary.Post', on_delete=models.CASCADE, related_name='categories')
    
    def __str__(self):
        return self.title    

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=100, default='')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    approved_post = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('diary.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

# Create your models here.
