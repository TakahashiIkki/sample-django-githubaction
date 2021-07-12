# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path

from app.blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog', blog_views.BlogViewSets.as_view({'post': 'create'}))
]
