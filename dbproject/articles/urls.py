from django.urls import path

from .views import ArticleCreate, ArticleUpdate, ArticleDelete, read_article, delete_article, HomePageView, SearchResultView, ArticleView, CategoryView, create_category
from django.views.generic.base import TemplateView

urlpatterns = [
    path('article/new/', ArticleCreate.as_view(), name="create-article"),
    path('article/<int:pk>/edit', ArticleUpdate.as_view(), name="edit-article"),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name="delete-article"),  
    path('read_article/', read_article),
    path('create_category/', create_category),
    path("", HomePageView.as_view(), name="home"),
    path("search_result/", SearchResultView.as_view(), name="search_result"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
]