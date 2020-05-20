# rename this file to views.py to use class based api view Using generic class-based views
# working class based api views Using generic class-based views
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer