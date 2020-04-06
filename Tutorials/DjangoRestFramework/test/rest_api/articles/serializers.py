from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')
        
    # def create(self, validated_data):
    #     validated_data['author_id'] = 1
    #     return super(ArticleSerializer, self).create(validated_data)