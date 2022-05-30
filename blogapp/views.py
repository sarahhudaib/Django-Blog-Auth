from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
)

from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer
# from .permissions import IsOwnerOrReadOnly


class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )


# class ArticlesDetailView(RetrieveUpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsOwnerOrReadOnly, )
