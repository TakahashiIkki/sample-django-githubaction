# -*- coding:utf-8 -*-
from django.db import models


class Blog(models.Model):
    title = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'

    class JSONAPIMeta:
        resource_name = 'blog'
