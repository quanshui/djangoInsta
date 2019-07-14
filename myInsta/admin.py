# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myInsta.models import Post, InstaUser, Comment, Like
# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Comment)
admin.site.register(Like)
