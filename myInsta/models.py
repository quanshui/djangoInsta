# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse

from django.contrib.auth.models import AbstractUser

# Create your models here.

class InstaUser(AbstractUser):
    profile_pic=ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        blank = True,
        null = True,
        )

class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='posts',
        blank = True,
        null = True,
    )

    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        blank = True,
        null = True,
        )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    posted_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    def __str__(self):
        return self.comment

class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='likes' #external ref to join table
    )
    
    def __str__(self):
        return 'Likes: ' + self.user.username + ' likes '