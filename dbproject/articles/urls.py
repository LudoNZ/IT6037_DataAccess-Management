from django.urls import path

from .views import create_article, update_article, delete_article, HomePageView, ArticleView, CategoryView, create_category, search_result
from django.views.generic.base import TemplateView

urlpatterns = [
    path('create_article/', create_article, name="create_article"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article"),
    path("article/<int:pk>/edit", update_article, name="update_article"),
    path('delete_article/<int:pk>/', delete_article, name="delete_article"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article"),
    path('create_category/', create_category),
    path("", HomePageView.as_view(), name="home"),
    path("article/", search_result, name="search"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
]