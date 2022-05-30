from rest_framework import serializers
from blogapp.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('title','date_created','updated' ,'author', 'content', 'published')