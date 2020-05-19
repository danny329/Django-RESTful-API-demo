from django.urls import  path
from appone import views
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import routers

#working class based api views
urlpatterns = [

    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


# #working api_views() decorator on function based api views
# urlpatterns = [
#
#     path('articles/', views.article_list),
#     path('articles/<int:pk>/', views.article_details),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# #working function based api views
# urlpatterns = [
#
#     path('articles/', views.article_list),
#     path('articles/<int:pk>/', views.article_details),
# ]
