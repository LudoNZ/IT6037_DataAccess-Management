from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .models import Articles, Category

# Create your views here.

@csrf_exempt
def create_article(request):
    name = request.POST['name']
    about = request.POST['about']

    article = Articles(name=name, about=about)
    article.save()

    print(article)

    return HttpResponse("Hello create article View")

def read_article(request):
    articles = Articles.objects.all()
    response = []

    for a in articles:
        print(a.name, a.about)
        response.append({'name':a.name, 'about':a.about, 'category':a.category, 'type':a.type})

    return JsonResponse(response, safe=False)

@csrf_exempt
def update_article(request):
    name = request.POST['name']
    about = request.POST['about']
    category = request.POST['category']
    type = request.POST['type']

    print(name, about)

    article = Articles.objects.get(name=name)
    article.about = about
    article.category = category
    article.type = type

    fields = {'demo field':'new value', 'another field':'replaced'}
    article.fields = fields

    print(article)
    
    article.save()

    return HttpResponse("Hello update article TestView")

@csrf_exempt
def delete_article(request):
    name = request.POST['name']
    article = Articles.objects.get(name=name)
    article.delete()

    return HttpResponse("deleted")


@csrf_exempt
def create_category(request):
    name = request.POST['name']

    category = Category(name=name)
    category.save()

    response = "Category created: " + name

    return HttpResponse(response)


class HomePageView(TemplateView):

    def get(self, request):

        return render(request, "articles\home.html")

class SearchResultView(TemplateView):

    def get(self, request):

        return render(request, "articles\search_result.html")

class ArticleView(TemplateView):

    def get(self, request, pk):

        article = Articles.objects.get(id=pk)

        context = {'article':article}

        return render(request, "articles/article.html", context)

class CategoryView(TemplateView):

    def get(self, request, pk):

        category = Category.objects.get(id=pk)
        articles = Articles.objects.all()

        for a in articles:
            a.about = a.about[:150] + "...."

        context = {'category':category, 'articles':articles}

        return render(request, "articles/category.html", context)