from django.urls import path

from .views import testView

urlpatterns = [
    path('', testView),
]