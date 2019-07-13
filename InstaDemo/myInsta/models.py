# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to = 'static/images/posts')