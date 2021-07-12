from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'text', 'created_at',)

    class JSONAPIMeta:
        resource_name = 'blog'
