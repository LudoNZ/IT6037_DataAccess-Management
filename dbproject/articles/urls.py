from django.urls import path

from .views import create_article, read_article, update_article, delete_article, HomePageView, SearchResultView, ArticleView, CategoryView, create_category
from django.views.generic.base import TemplateView

urlpatterns = [
    path('create_article/', create_article, name="create_article"),
    path('read_article/', read_article),
    path("article/<int:pk>/edit", update_article, name="update_article"),
    path('delete_article/<int:pk>/', delete_article, name="delete_article"),
    path('create_category/', create_category),
    path("", HomePageView.as_view(), name="home"),
    path("search_result/", SearchResultView.as_view(), name="search_result"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
]