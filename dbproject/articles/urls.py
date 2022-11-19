from django.urls import path

from .views import create_article, read_article, update_article, delete_article, HomePageView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('create_article/', create_article),
    path('read_article/', read_article),
    path('update_article/', update_article),
    path('delete_article/', delete_article),
    path("", HomePageView.as_view(), name="home"),
]