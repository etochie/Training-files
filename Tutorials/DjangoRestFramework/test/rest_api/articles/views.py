from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

from .models import Article, Author
from .serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # def perform_create(self, serializer):
    #     author = get_object_or_404(Author, id=self.request.data.get('author_id'))
    #     return serializer.save()


    