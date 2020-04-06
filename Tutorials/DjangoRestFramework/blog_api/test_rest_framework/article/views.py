from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import Article, Author
from .serializers import ArticleSerializer


# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         # параметр many сообщает serializer-у, что он будет обрабатывать не одну статью
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})

#     def post(self, request):
#         article = request.data.get('article')

#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({'success': "Article '{}' created successfully.".format(article_saved.title)})

#     def put(self, request, pk):
#         # получаем объект
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         # параметр partial для обновления некоторых полей, а не всех сразу
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()

#         return Response({
#             "success": "Article '{}' updated successfully.".format(article_saved.title)
#         })

#     def delete(self, request, pk):
#         # получаем объект
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "message": "Article {} has been deleted.".format(article.title)
#         }, status=204)


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    # def perform_create(self, serializer):
    #     author = get_object_or_404(Author, id=self.request.data.get('author_id'))
    #     return serializer.save(author=author)