# rename this file to class based api view.py to use api_view() in function based api view
# api_view() in function based api view


from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


#article list views [get,post]
@api_view(['GET', 'POST'])
def article_list(request, format=None):
    if request.method=='GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# article detail views [get,put,delete]
@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk, format=None):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


