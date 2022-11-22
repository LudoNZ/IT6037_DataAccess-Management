from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from .models import Articles, Category
from django.urls import reverse_lazy

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


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = "articles\create-article.html"
    success_url="/home"
    fields =["name", "about", "category", "type", "fields"]

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = "articles\edit-article.html"
    success_url="/home"
    fields =["name", "about", "category", "type", "fields"]

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = "articles/delete-article.html"
    success_url=reverse_lazy("home")


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

        context = {'category':category, 'articles':articles}

        return render(request, "articles/category.html", context)