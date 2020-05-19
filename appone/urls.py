from django.urls import  path
from appone import views
# from rest_framework import routers


urlpatterns = [

    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_details),
]

# #working function based api views and api_views() decorator on function based api views
# urlpatterns = [
#
#     path('articles/', views.article_list),
#     path('articles/<int:pk>/', views.article_details),
# ]