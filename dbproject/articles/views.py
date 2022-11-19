from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def create_article(request):
    return HttpResponse("Hello create article View")

def read_article(request):
    return HttpResponse("Hello read article View")

def update_article(request):
    return HttpResponse("Hello update article TestView")

def delete_article(request):
    return HttpResponse("Hello delete article TestView")

class HomePageView(TemplateView):

    def get(self, request):

        return render(request, "articles\home.html")