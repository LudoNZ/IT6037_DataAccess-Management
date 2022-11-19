from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .models import Articles

# Create your views here.

@csrf_exempt
def create_article(request):
    name = request.POST['name']
    about = request.POST['about']

    print(name, about)

    article = Articles(name=name, about=about)
    article.save()

    print(article)

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